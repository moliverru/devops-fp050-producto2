
import os
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer


class Manejador(BaseHTTPRequestHandler):
    def do_GET(self):
        nombre_pod = socket.gethostname()
        mensaje = f"DevOps FP050 - Respuesta desde el pod {nombre_pod}\n"

        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(mensaje.encode("utf-8"))


if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 8080))
    servidor = HTTPServer(("0.0.0.0", puerto), Manejador)

    print(f"Servidor iniciado en el puerto {puerto}", flush=True)
    servidor.serve_forever()
