from abc import ABC, abstractmethod


class WebPage(ABC):
    """Interfaz común para todos los tipos de páginas."""

    @abstractmethod
    def render(self) -> str:
        pass


class LandingPage(WebPage):
    def render(self) -> str:
        return """
        <!DOCTYPE html>
        <html>
        <head><title>Landing Page</title></head>
        <body>
            <header><h1>Bienvenido a Nuestro Producto</h1></header>
            <section>
                <h2>Características</h2>
                <ul>
                    <li>Rápido y eficiente</li>
                    <li>Fácil de usar</li>
                    <li>Precio accesible</li>
                </ul>
            </section>
            <footer><button>Comprar Ahora</button></footer>
        </body>
        </html>
        """


class BlogPage(WebPage):
    def render(self) -> str:
        return """
        <!DOCTYPE html>
        <html>
        <head><title>Blog</title></head>
        <body>
            <header><h1>Mi Blog</h1></header>
            <nav>
                <a href="#">Inicio</a> | <a href="#">Artículos</a> | <a href="#">Contacto</a>
            </nav>
            <article>
                <h2>Último Post</h2>
                <p>Contenido del artículo...</p>
            </article>
            <footer><p>© 2024 Mi Blog</p></footer>
        </body>
        </html>
        """


class ContactPage(WebPage):
    def render(self) -> str:
        return """
        <!DOCTYPE html>
        <html>
        <head><title>Contacto</title></head>
        <body>
            <header><h1>Contáctenos</h1></header>
            <form>
                <label>Nombre: <input type="text" name="nombre"></label><br>
                <label>Email: <input type="email" name="email"></label><br>
                <label>Mensaje: <textarea name="mensaje"></textarea></label><br>
                <button type="submit">Enviar</button>
            </form>
            <footer><p>Tel: 1234-5678</p></footer>
        </body>
        </html>
        """


class WebPageCreator(ABC):
    """Creador abstracto que define el factory method."""

    @abstractmethod
    def create_page(self) -> WebPage:
        pass

    def render_page(self) -> str:
        page = self.create_page()
        return page.render()


class LandingPageCreator(WebPageCreator):
    def create_page(self) -> WebPage:
        return LandingPage()


class BlogPageCreator(WebPageCreator):
    def create_page(self) -> WebPage:
        return BlogPage()


class ContactPageCreator(WebPageCreator):
    def create_page(self) -> WebPage:
        return ContactPage()


def client_code(creator: WebPageCreator) -> None:
    print(creator.render_page())


if __name__ == "__main__":
    print("=== Landing Page ===")
    client_code(LandingPageCreator())
    print("\n=== Blog ===")
    client_code(BlogPageCreator())
    print("\n=== Contacto ===")
    client_code(ContactPageCreator())