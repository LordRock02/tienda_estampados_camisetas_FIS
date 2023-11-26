from website import create_app
import sys

sys.path.insert(0, '/Users/roger/workspace/tienda_estampados_camisetas_FIS/website')

app = create_app()

if __name__ == '__main__':
    app.run()