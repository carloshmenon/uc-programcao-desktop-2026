from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QHeaderView

from model.usuario_model import UsuarioModel


from controller.clientes_controller import ClientesController
from controller.bicicletas_controller import BicicletasController
from controller.servicos_controller import ServicosController
from controller.relatorios_controller import RelatoriosController


class HomeController:

    def __init__(self):

        loader = QUiLoader()

        file = QFile("view/home.ui")
        file.open(QFile.ReadOnly)

        self.window = loader.load(file)
        file.close()

        self.model = UsuarioModel

        # Página inicial
        self.window.stackedWidget.setCurrentIndex(0)

        # USUÁRIOS
        self.window.btnMenuUsuarios.clicked.connect(
            self.listar_usuarios
        )

        self.window.btnUsuariosNovo.clicked.connect(
            self.novo_usuario
        )

        self.window.btnCadUsuarioCadastrar.clicked.connect(
            self.inserir_usuario
        )

        self.window.tabelaUsuarios.cellDoubleClicked.connect(
            self.abrir_edicao
        )

        # CLIENTES
        self.window.btnMenuClientes.clicked.connect(
            self.abrir_clientes
        )

        # BICICLETAS
        self.window.btnMenuBicicletas.clicked.connect(
            self.abrir_bicicletas
        )

        # SERVIÇOS
        self.window.btnMenuServicos.clicked.connect(
            self.abrir_servicos
        )

        # RELATÓRIOS
        self.window.btnMenuRelatorios.clicked.connect(
            self.abrir_relatorios
        )

    # =========================
    # USUÁRIOS
    # =========================

    def listar_usuarios(self):

        self.window.stackedWidget.setCurrentIndex(1)

        dados = self.model.listar(self)

        self.window.tabelaUsuarios.setRowCount(len(dados))

        # Remove números laterais
        self.window.tabelaUsuarios.verticalHeader().setVisible(False)

        # Selecionar linha inteira
        self.window.tabelaUsuarios.setSelectionBehavior(
            self.window.tabelaUsuarios.SelectionBehavior.SelectRows
        )

        # Ajustar colunas
        self.window.tabelaUsuarios.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        for linha, usuario in enumerate(dados):

            self.window.tabelaUsuarios.setItem(
                linha,
                0,
                QTableWidgetItem(str(usuario[0]))
            )

            self.window.tabelaUsuarios.setItem(
                linha,
                1,
                QTableWidgetItem(usuario[1])
            )

            self.window.tabelaUsuarios.setItem(
                linha,
                2,
                QTableWidgetItem(usuario[2])
            )

            self.window.tabelaUsuarios.setItem(
                linha,
                3,
                QTableWidgetItem(usuario[3])
            )

    def novo_usuario(self):

        self.window.stackedWidget.setCurrentIndex(2)

    def inserir_usuario(self):

        nome = self.window.inputCadUsuarioNome.text()

        email = self.window.inputCadUsuarioEmail.text()

        senha = self.window.inputCadUsuarioSenha.text()

        confirmar_senha = (
            self.window.inputCadUsuarioConfirmarSenha.text()
        )

        if senha == confirmar_senha:

            self.model.inserir(
                self,
                nome,
                email,
                senha
            )

            self.listar_usuarios()

        else:
            print("As senhas não são iguais")

    def abrir_edicao(self, row):

        id_usuario = int(
            self.window.tabelaUsuarios.item(row, 0).text()
        )

        nome = self.window.tabelaUsuarios.item(row, 1).text()

        email = self.window.tabelaUsuarios.item(row, 2).text()

        senha = self.window.tabelaUsuarios.item(row, 3).text()

        self.window.stackedWidget.setCurrentIndex(2)

        self.window.inputCadUsuarioNome.setText(nome)

        self.window.inputCadUsuarioEmail.setText(email)

        self.window.inputCadUsuarioSenha.setText(senha)

    # =========================
    # TELAS
    # =========================

    def abrir_clientes(self):
        # 1. Cria a tela passando a janela principal como referência
        self.tela_clientes = ClientesController(main_window=self.window)
        
        # 2. LOCALIZA A TABELA DE FORMA SEGURA (Mapeando possíveis nomes)
        tabela = None
        
        if hasattr(self.window, 'tabelaClientes'):
            tabela = self.window.tabelaClientes
        elif hasattr(self.window, 'tableWidget'):
            tabela = self.window.tableWidget
            print("AVISO: Usando o nome padrão 'tableWidget' para a tabela de clientes.")
        elif hasattr(self.window, 'tabela_clientes'):
            tabela = self.window.tabela_clientes
        
        # 3. CONECTA SÓ SE DOIS REQUISITOS FOREM ATENDIDOS
        if tabela is not None:
            # Vincula o duplo clique da tabela encontrada à função de edição
            tabela.cellDoubleClicked.connect(self.tela_clientes.abrir_edicao)
            
            # ATENÇÃO: Ajustamos o ClientesController para usar a tabela correta dinamicamente
            # Substituindo temporariamente a referência interna dele
            self.window.tabelaClientes = tabela 
        else:
            print("\n[ERRO CRÍTICO] A tabela de clientes não foi encontrada com os nomes testados!")
            print("Componentes disponíveis na sua interface Home:")
            # Mostra no terminal todos os componentes que existem na tela para você achar o nome da tabela
            for comp in dir(self.window):
                if not comp.startswith('_'):
                    print(f" - {comp}")
        
        # 4. Configura o botão de "Novo Cliente" de forma segura
        if hasattr(self.window, 'btnNovoCliente'):
            self.window.btnNovoCliente.clicked.connect(lambda: self.window.stackedWidget.setCurrentIndex(2))
        
        # 5. Tenta listar os clientes
        try:
            self.tela_clientes.listar_clientes()
        except Exception as e:
            print(f"Aviso ao listar: {e} (Pode ser que a aba da tabela ainda precise de ajuste de index)")

    def abrir_bicicletas(self):

        self.tela_bicicletas = BicicletasController()
        self.tela_bicicletas.show()

    def abrir_servicos(self):

        self.tela_servicos = ServicosController()
        self.tela_servicos.show()

    def abrir_relatorios(self):

        self.tela_relatorios = RelatoriosController()
        self.tela_relatorios.show()

    # =========================
    # SHOW
    # =========================

    def show(self):

        self.window.show()