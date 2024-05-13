from manim import *

class TranslationAnimation(Scene):
    def construct(self):
        # Define encoder animation (trapezoidal shape)
        encoder_animation = Polygon(
            np.array([0, 0, 0]),
            np.array([-2, 1, 0]),
            np.array([-2, -2, 0]),
            np.array([0, -1, 0]),
            np.array([0, 0, 0]),
            color=BLUE,
            fill_opacity=0.5
        )
        encoder_text = Tex("Encoder").next_to(encoder_animation, UP)
        english_words = Text("Machine learning is a subfield of artificial intelligence.").rotate(PI/2).next_to(encoder_animation, LEFT, buff=0.4)
        # Define decoder animation (trapezoidal shape)
        decoder_animation = Polygon(
            np.array([1, 0, 0]),
            np.array([3, 1, 0]),
            np.array([3, -2, 0]),
            np.array([1, -1, 0]),
            np.array([1, 0, 0]),
            color=RED,
            fill_opacity=0.5
        )
        decoder_text = Tex("Decoder").next_to(decoder_animation, UP)        
        french_words = Text("L'apprentissage automatique est un sous-domaine de l'intelligence artificielle.").rotate(-PI/2).next_to(decoder_animation, RIGHT, buff=0.4)
        # Show encoder and decoder animations and text simultaneously
        self.play(Create(encoder_animation), Write(encoder_text), Create(decoder_animation), Write(decoder_text),Write(english_words.scale(0.3)),Write(french_words.scale(0.3)))

        # Wait for a moment
        self.wait(1)

# Render the scene
scene = TranslationAnimation()
# scene.render("translation_animation.gif", renderer=renderer(file_writer_config={'flush_cache_once': False}))
scene.render() 
