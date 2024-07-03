from datetime import datetime
from hashtag import Hashtag



class Post:
    """Constructor for the Post class.

    The constructor for the Post class is used to create a new post.

    Syntax
    ------
        post = Post(title, author, date_published, hashtags)
    
    Parameters
    ----------
    title : str
        The title of the post.
    author : str
        The author of the post.
    date_published : datetime
        The date the post was published.
    hashtags : set, optional
        A set of hashtags associated with the post.
    
    Returns
    -------
        The new post.

    Example
    -------
        post = Post("Vacaciones en Bali", "John Doe", datetime.now(), {Hashtag.TRAVEL})
    """
    def __init__(self, title, author, date_published, hashtags=None):
        if not isinstance(title, str):
            raise TypeError("El título debe ser una cadena de caracteres.")
        if not isinstance(author, str):
            raise TypeError("El autor debe ser una cadena de caracteres.")
        if not isinstance(date_published, datetime):
            raise TypeError("La fecha de publicación debe ser un objeto datetime.")
        if date_published > datetime.now():
            raise ValueError("La fecha de publicación no puede ser futura.")
        if hashtags:
            for hashtag in hashtags:
                if not isinstance(hashtag, Hashtag):
                    raise ValueError("Todos los hashtags deben ser del tipo Hashtag.")
        
        self.title = title
        self.author = author
        self.date_published = date_published
        self.hashtags = hashtags if hashtags else set()
        self.comments = []

    def add_hashtag(self, hashtag):
        """Adds a hashtag to the post if not already present."""
        if isinstance(hashtag, Hashtag):
            self.hashtags.add(hashtag)

    def add_comment(self, comment):
        """Adds a comment to the post."""
        self.comments.append(comment)

    def __eq__(self, other):
        """Check equality based on title, author, and date_published."""
        if not isinstance(other, Post):
            return NotImplemented
        return (self.title == other.title and 
                self.author == other.author and 
                self.date_published == other.date_published)

    def __str__(self):
        """String representation of the post."""
        hashtags_str = sorted([hashtag.name for hashtag in self.hashtags])
        return f"{self.title} de {self.author} con hashtags {hashtags_str} y comentarios {self.comments}."

def main():
    """Function main of the module to test the Class Post."""
    print("=================================================================.")
    print("Test Case 1: Check Class Post - Initialization.")
    print("=================================================================.")
    
    date_published = datetime.now()
    hashtags = {Hashtag.TRAVEL, Hashtag.FOOD}
    
    try:
        post = Post("Vacaciones en Bali", "John Doe", date_published, hashtags)
        print("Test PASS. The Post has been correctly initialized.")
    except Exception as e:
        print(f"Test FAIL. {e}")
    
    print("=================================================================.")
    print("Test Case 2: Check Class Post - Add Hashtag.")
    print("=================================================================.")
    
    try:
        post.add_hashtag(Hashtag.FASHION)
        if Hashtag.FASHION in post.hashtags:
            print("Test PASS. The Hashtag has been correctly added.")
        else:
            print("Test FAIL. The Hashtag has not been added.")
    except Exception as e:
        print(f"Test FAIL. {e}")
    
    print("=================================================================.")
    print("Test Case 3: Check Class Post - Add Comment.")
    print("=================================================================.")
    
    try:
        post.add_comment("¡Qué hermoso lugar!")
        if "¡Qué hermoso lugar!" in post.comments:
            print("Test PASS. The Comment has been correctly added.")
        else:
            print("Test FAIL. The Comment has not been added.")
    except Exception as e:
        print(f"Test FAIL. {e}")
    
    print("=================================================================.")
    print("Test Case 4: Check Class Post - Equality.")
    print("=================================================================.")
    
    try:
        another_post = Post("Vacaciones en Bali", "John Doe", date_published, hashtags)
        if post == another_post:
            print("Test PASS. The equality method works correctly.")
        else:
            print("Test FAIL. The equality method does not work correctly.")
    except Exception as e:
        print(f"Test FAIL. {e}")
    
    print("=================================================================.")
    print("Test Case 5: Check Class Post - String Representation.")
    print("=================================================================.")
    post2 = Post("Vacaciones en Bali", "John Doe", datetime(2023, 5, 20), {Hashtag.TRAVEL, Hashtag.FOOD})
    post2.add_comment("¡Qué lugar tan hermoso!")
    post2.add_comment("Espero poder ir algún día.")

    expected_str = "Vacaciones en Bali de John Doe con hashtags ['FOOD', 'TRAVEL'] y comentarios ['¡Qué lugar tan hermoso!', 'Espero poder ir algún día.']."
    if str(post2) == expected_str:
        print("Test PASS. El formato legible de la publicación destacada se ha implementado correctamente.")
        print(str(post2))
    else:
        print("Test FAIL. Revisar el método __str__()." + " RESULTADO: " + str(post2))

if __name__ == "__main__":
    main()
