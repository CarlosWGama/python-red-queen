from gtts import gTTS
import playsound
import os
from datetime import datetime
import wikipedia
class RedQueen:
    pass

    def __falar(self, texto):
        print('RedQueen:', texto)

        #Exemplo
        #Cria audio
        audio = gTTS(texto, lang='pt')
        audio.save('./arquivo.mp3')

        #Executa
        playsound.playsound('./arquivo.mp3')

        #Remove
        os.remove('./arquivo.mp3')

    def executar(self):
        self.__falar('Em que posso ajudá-lo?')
        wikipedia.set_lang('pt')

        while(True):
            comando = input('Você: ').lower()

            #Comando encerrar
            if (comando in ['sair', 'tchau']):
                self.__falar('Até mais')
                break
            #Operação matemática
            elif('quanto é' in comando):
                operacao = comando[8:] #Pegar todos caracteres após quanto é
                resultado = eval(operacao)
                self.__falar('O resultado é ' + str(resultado))

            #Dia
            elif('dia é hoje' in comando):
                agora = datetime.now()
                self.__falar('Hoje é ' + str(agora.day) + ' do ' + str(agora.month) + ' de ' + str(agora.year))

            #horas
            elif('horas são' in comando):
                agora = datetime.now()
                self.__falar('Agora são ' + str(agora.hour) + ' horas e ' + str(agora.minute) + ' minutos')

            #Busca pessoas
            elif('quem foi' in comando):
                pessoa = comando[8:]
                self.__falar(wikipedia.summary(pessoa, sentences=1))
            
            #Busca termos
            elif('o que é' in comando):
                termo = comando[7:]
                self.__falar(wikipedia.summary(termo, sentences=1))

            else:
                self.__falar('Não sei como ajudá-lo')
