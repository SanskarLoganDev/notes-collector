from website import create_app

app = create_app()
# only if we run this file and not import this file, the code inside if will run
if __name__ == '__main__':
    app.run(debug=True)  # run our application and start up a web server and debug=true means it reruns the we server when
    # make changes to the python code