class Review:
    def __init__(self, user_name):
        # Inicializa con el nombre del usuario y una reseña vacía
        self.user_name = user_name
        self.review_text = ""
        self.id_unico = uuid.uuid4

    def write_review(self, text):
        # Escribe una nueva reseña
        self.review_text = text

    def edit_review(self, new_text):
        # Edita la reseña existente
        self.review_text = new_text

instancia = Review()
print(instancia.id_unico)