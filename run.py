from web import create_app

# MENJALANKAN SERVER FLASK
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
# AKHIR MENJALANKAN SERVER FLASK