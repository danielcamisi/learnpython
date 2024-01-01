from PyQt5 import uic, QtWidgets #Este comando importa os recursos presentes no PyQt5, o UIC = User Interface Controle, e QtWidgets é em si os recursos. se seguirmos com isso os próximos comandos aplicaram funções aos recursos do Qt5

def executar():

    salario=form.infoSalario.text()
    salario=float(salario)
    desconto=form.infoDescontos.text()
    desconto=float(desconto)

    resultado= salario-desconto

    form.lblResultado.setText(str(resultado))

app=QtWidgets.QApplication([]) #App é uma variável que recebe os widgets do Qt, e o QApplication atribuirá as definidas funções
form=uic.loadUi("projetosalario.ui")
form.btnCalcular.clicked.connect(executar)

form.show()
app.exec()