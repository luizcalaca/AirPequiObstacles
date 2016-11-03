# airpequiobstacles

O AirPequiObstacles tem o intuito de auxiliar um deficiente visual a desviar de obstáculos aéreos, tais como: orelhão, postes, placas e outros; obstáculos estes não obtidos pela bengala (comumente usada).

O software aqui codificado foi desenvolvido em Python 3, na Raspberry Pi 3. Ele realiza o controle do recebimento da distância de um obstáculo -- obtido via sensor ultrassônico -- e, ainda, caso ocorra uma distância menor que alimite: aciona um alerta sonoro e vibratório. Quando tal, conecta-se ao Firebase (Banco Real Time do Google) e envia a data e distância.
