from manim import *

class FuncaoInversa(MovingCameraScene):
    def construct(self):

        # configuracao de cores, titulos e logo
        self.camera.frame.save_state()

        # configuracao de cores, titulos e logo
        mycolor = ManimColor('#071E25')
        self.camera.background_color = mycolor
        
        # configuracao logo
        img = ImageMobject('ifes.jpeg')
        img.scale(1)  
        img.shift(3.3*DOWN + 5.6*RIGHT)  
        self.add(img) 

        # Título
        titulo = Tex("Invertendo uma função", font_size=48).to_edge(RIGHT + UP)
        self.play(Write(titulo))
        self.wait(1)

        turma = Tex("Licenciatura em Matemática" , font_size=35).next_to(titulo, DOWN, buff=0.1)
        self.play(Write(turma))
        self.wait(1)

        prof = Tex("Prof. Alex Jordane" , font_size=30).next_to(turma, DOWN, buff=0.1)
        self.play(Write(prof))
        self.wait(1)

        texto_1 = Tex("Vamos traçar o gráfico da função $f(x) = x^2$.", font_size=30).to_edge(RIGHT + 4*UP)
        self.play(Write(texto_1))
        self.wait(2)
        self.play(Unwrite(texto_1))

        # 1. O Palco: Construindo os eixos
        # É oportuno definir limites que acomodem bem a parábola
        fator = 1
        eixos = Axes(
            x_range=[-4, 8.9, 1],
            y_range=[-0.9, 8.9, 1],
            axis_config={"color": BLUE},
            x_length=8 * fator,
            y_length=8 * fator,
            # Mostramos apenas alguns números para não poluir a tela
            x_axis_config={"numbers_to_include": [-2, 2]}, 
            y_axis_config={"numbers_to_include": [4]}
        ).add_coordinates()
        
        rotulos_eixos = eixos.get_axis_labels(x_label="x", y_label="y")
        
        # Passo 1: Desenhando f(x) = x^2
        grafico_completo = eixos.plot(lambda x: x**2, x_range=[-3, 3], color=YELLOW)
        titulo = MathTex("f(x) = x^2").to_edge(UP + LEFT)

        dominio_texto = MathTex(r"f: \mathbb{R} \to \mathbb{R}").scale(0.8)
        
        # Posicionamos exatamente abaixo do título
        dominio_texto.next_to(titulo, DOWN)

        self.play(Create(eixos), Write(rotulos_eixos))
        self.play(Write(titulo), Write(dominio_texto), Create(grafico_completo), run_time=2)
        self.wait(3)

        texto_1 = Tex(r"Vamos marcar dois pontos da função:\\$(-2, 4)$ e $(2, 4)$.", font_size=30).to_edge(RIGHT + 4*UP)
        self.play(Write(texto_1))
        self.wait(2)
        self.play(Unwrite(texto_1))

        # Passo 2: Mostrando que não é injetora
        # Usamos DashedLine indicando o ponto de início e o de fim
        reta_y4 = DashedLine(
            start=eixos.c2p(-2, 4), 
            end=eixos.c2p(2, 4), 
            color=RED
        )
        
        ponto1 = Dot(eixos.c2p(-2, 4), color=RED)
        ponto2 = Dot(eixos.c2p(2, 4), color=RED)
        
        # O comando get_vertical_line já cria uma linha tracejada naturalmente
        linha_vert1 = eixos.get_vertical_line(ponto1.get_center(), color=RED)
        linha_vert2 = eixos.get_vertical_line(ponto2.get_center(), color=RED)

        self.play(Create(reta_y4))
        self.play(FadeIn(ponto1, ponto2))
        self.play(Create(linha_vert1), Create(linha_vert2))
        
        coord1 = MathTex("(-2, 4)", color=RED).scale(0.7)
        coord2 = MathTex("(2, 4)", color=RED).scale(0.7)

        coord1.next_to(ponto1, UP + LEFT, buff=0.1)
        coord2.next_to(ponto2, UP + RIGHT, buff=0.1)

        self.play(Write(coord1), Write(coord2))

        self.wait(2)

        texto_1 = Tex(r"Aqui é possível notar que\\ a função não é injetora, \\ pois $y=4$ é imagem de \\$x=-2$ e de $x=2$.", font_size=30).to_edge(RIGHT + 4*UP)
        self.play(Write(texto_1))
        self.wait(2)
        self.play(Unwrite(texto_1))

        texto_1 = Tex(r"Vamos \textbf{inverter} o gráfico.", font_size=30).to_edge(RIGHT + 4*UP)
        self.play(Write(texto_1))
        self.wait(2)
        self.play(Unwrite(texto_1))

        grupo_naoinversa = VGroup(eixos, rotulos_eixos, grafico_completo, reta_y4, ponto1, ponto2, linha_vert1, linha_vert2, coord1, coord2)

        self.play(
            grupo_naoinversa.animate.flip(axis=UP + RIGHT, about_point=eixos.c2p(4, 4.5)),
            run_time=3  # Um tempo um pouco maior para a transformação ser apreciada
        )
        self.wait(3)

        texto_1 = Tex(r"Aqui é possível notar que\\ a representação não é uma função, \\ pois temos duas imagens ($-2$ e $2$)\\ para $x=4$.", font_size=30).to_edge(RIGHT + 4*UP)
        self.play(Write(texto_1))
        self.wait(2)
        self.play(Unwrite(texto_1))


        self.play(
            grupo_naoinversa.animate.flip(axis=UP + RIGHT, about_point=eixos.c2p(4, 4.5)),
            run_time=3  # Um tempo um pouco maior para a transformação ser apreciada
        )    
        self.wait(2)

        texto_1 = Tex(r"Vamos restringir o domínio \\ e o contradomínio para forçar \\ a bijetividade da função. \\ Se $D(f)=\mathbb{R}^+$ e $CD(f)=\mathbb{R}^+$, \\a função se torna bijetora.", font_size=30).to_edge(RIGHT + 4*UP)
        self.play(Write(texto_1))
        self.wait(2)
        self.play(Unwrite(texto_1))

        # Passo 3: Delimitando o Domínio (Tornando Injetora)
        # Criamos uma nova versão do gráfico, apenas com o lado positivo
        grafico_injetivo = eixos.plot(lambda x: x**2, x_range=[0, 3], color=GREEN)

        dominio_bijetiva_texto = MathTex(r"f: \mathbb{R}^+ \to \mathbb{R}^+").scale(0.8)

        dominio_bijetiva_texto.move_to(dominio_texto)

        self.play(
            # Apagamos as marcações antigas
            FadeOut(reta_y4, ponto1, linha_vert1, linha_vert2, coord1),
            # Transformamos a parábola inteira na "metade" verde
            ReplacementTransform(grafico_completo, grafico_injetivo),
            ReplacementTransform(dominio_texto, dominio_bijetiva_texto),
            run_time=2
        )
        self.wait(2)

        # --- NOVO TRECHO: Focando no 1º Quadrante ---
        
        # 1. Criamos os novos eixos, agora apenas do 0 para a frente
        eixos_q1 = Axes(
            x_range=[-0.8, 9, 1],
            y_range=[-0.8, 9, 1],
            x_length=7 * fator,
            y_length=7 * fator,
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": [1, 2, 3, 4, 5, 6, 7, 8]},
            y_axis_config={"numbers_to_include": [1, 2, 3, 4, 5, 6, 7, 8]}
        )
        
        # Movemos esses novos eixos para o canto inferior esquerdo,
        # assim o 1º quadrante ocupa quase a tela toda
        eixos_q1.to_edge(DOWN)
        rotulos_q1 = eixos_q1.get_axis_labels(x_label="x", y_label="y")


        # 2. Desenhamos o mesmo gráfico, mas usando as coordenadas dos novos eixos
        grafico_q1 = eixos_q1.plot(lambda x: x**2, x_range=[0, 3], color=GREEN)

        # 3. A Animação da metamorfose
        self.play(
            FadeOut(ponto2, coord2),
            ReplacementTransform(eixos, eixos_q1),
            ReplacementTransform(rotulos_eixos, rotulos_q1),
            ReplacementTransform(grafico_injetivo, grafico_q1),
            run_time=2.5 # Um tempo um pouco maior para a transição ficar majestosa
        )
        self.wait(2)

        texto_1 = Tex(r"Vamos, novamente, \textbf{inverter} o gráfico.", font_size=30).to_edge(RIGHT + 4*UP)
        self.play(Write(texto_1))
        self.wait(2)
        self.play(Unwrite(texto_1))

        # --- Passo 6: O Giro (Trocando os Eixos) ---
        
        numeros_antigos = VGroup(eixos_q1.get_x_axis().numbers, eixos_q1.get_y_axis().numbers)

        # Ocultamos os rótulos antigos para evitar que fiquem espelhados
        
        # Agrupamos os eixos e o gráfico verde para que se movam como um corpo único
        grupo_inversa = VGroup(eixos_q1, grafico_q1, rotulos_q1)
        
        # A MÁGICA DO MANIM:
        # Para trocar os eixos de lugar perfeitamente, refletimos (flip) o grupo
        # na direção diagonal (UP + RIGHT). 
        # O 'about_point' garante que a origem (0,0) fique presa no lugar, 
        # como se fosse um prego no papel.
        self.play(
            grupo_inversa.animate.flip(axis=UP + RIGHT, about_point=eixos_q1.c2p(0, 0)),
            run_time=3  # Um tempo um pouco maior para a transformação ser apreciada
        )
        self.wait(2)

        self.play(
                    eixos_q1.get_x_axis().numbers.animate.set_opacity(0),
                    eixos_q1.get_y_axis().numbers.animate.set_opacity(0),
                    FadeOut(rotulos_q1))
        
        rotulos_q1 = eixos_q1.get_axis_labels(x_label="y", y_label="x")

        eixos_fixos = Axes(
            x_range=[-0.8, 9, 1],
            y_range=[-0.8, 9, 1],
            x_length=7 * fator,
            y_length=7 * fator,
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": [1, 2, 3, 4, 5, 6, 7, 8]},
            y_axis_config={"numbers_to_include": [1, 2, 3, 4, 5, 6, 7, 8]}
        ).to_edge(DOWN)
        
        # Coletamos os números e rótulos desse novo eixo
        numeros_novos = VGroup(eixos_fixos.get_x_axis().numbers, eixos_fixos.get_y_axis().numbers, rotulos_q1)

        # Criamos o título da nova função
        titulo_inversa = MathTex(r"f^{-1}(x) = \sqrt{x}", color=GREEN).to_edge(6*DOWN + RIGHT)
        
        # Fazemos tudo aparecer suavemente
        self.play(FadeIn(numeros_novos))
        self.wait(1)
        self.play(Write(titulo_inversa))
        self.wait(1)

        # --- Passo 8: Traçando a original f(x) ---
        
        # Usamos o nosso eixo limpo para desenhar a parábola amarela original

        texto_1 = Tex(r"Voltemos com a função $f(x) = x^2$.", font_size=30).to_edge(RIGHT + 4*UP)
        self.play(Write(texto_1))
        self.wait(2)
        self.play(Unwrite(texto_1))

        grafico_original = eixos_fixos.plot(lambda x: x**2, x_range=[0, 3], color=YELLOW)

        rotulo_original = MathTex("f(x) = x^2", color=YELLOW).scale(0.8)

        rotulo_original.next_to(eixos_fixos.c2p(3, 7.5), UP + LEFT, buff=0.2)
        
        self.play(
            Create(grafico_original), 
            Write(rotulo_original), 
            run_time=2)
        
        self.wait(2)

        # --- Passo 9: O Eixo de Simetria (Reta y = x) ---
        
        # Criamos a reta tracejada partindo da origem e cortando o plano na diagonal
        texto_1 = Tex(r"Finalmente, vamos traçar a reta $y=x$,\\ eixo de simetria das funções \\ $f(x)=x^2$ e $f^{-1}(x)=\sqrt{x}$.", font_size=30).to_edge(RIGHT + 4*UP)
        self.play(Write(texto_1))
        self.wait(2)
        self.play(Unwrite(texto_1))

        reta_simetria = DashedLine(
            start=eixos_fixos.c2p(0, 0),
            end=eixos_fixos.c2p(7, 7),
            color=GRAY,
            dash_length=0.1 # Deixa os tracejados um pouco mais delicados
        )
        
        # Criamos o texto para identificar a reta
        rotulo_simetria = MathTex("y = x", color=GRAY).scale(0.8)
        
        # Posicionamos o rótulo próximo ao final da reta
        rotulo_simetria.next_to(eixos_fixos.c2p(6.5, 6.5), LEFT, buff=0.3)

        # Animamos o surgimento desse espelho geométrico
        self.play(Create(reta_simetria))
        self.wait(1)
        self.play(Write(rotulo_simetria)) 
        
        # Uma pausa final um pouco mais longa para que estudantes 
        # possam contemplar o quadro completo e a simetria perfeita
        self.wait(2)

        reta_s1 = DashedLine(
            start=eixos_fixos.c2p(3, 3), 
            end=eixos_fixos.c2p(4, 2), 
            color=RED
        )

        reta_s2 = DashedLine(
                    start=eixos_fixos.c2p(3, 3), 
                    end=eixos_fixos.c2p(2, 4), 
                    color=RED
                )
        
        ponto01 = Dot(eixos_fixos.c2p(3, 3), color=RED)
        ponto02 = Dot(eixos_fixos.c2p(2, 4), color=RED)
        ponto03 = Dot(eixos_fixos.c2p(4, 2), color=RED)

        coord01 = MathTex("(3, 3)", color=RED).scale(0.7)
        coord02 = MathTex("(2, 4)", color=RED).scale(0.7)
        coord03 = MathTex("(4, 2)", color=RED).scale(0.7)

        coord01.next_to(ponto01, RIGHT, buff=0.3)
        coord02.next_to(ponto02, UP + LEFT, buff=0.1)
        coord03.next_to(ponto03, DOWN + RIGHT, buff=0.1)

        # O comando get_vertical_line já cria uma linha tracejada naturalmente
        self.play(FadeIn(ponto01))

        self.play(Write(coord01))

        self.wait(1)

        self.play(Create(reta_s1), Create(reta_s2))
        
        self.play(FadeIn(ponto02, ponto03))

        self.play(Write(coord02), Write(coord03))

        self.wait(2)
