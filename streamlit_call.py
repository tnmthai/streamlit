from subprocess import Popen


def load_jupyter_server_extension(nbapp):
    """serve the streamlit Home"""
    Popen(
        [
            "streamlit",
            "run",
            "Home.py",
            "--browser.serverAddress=0.0.0.0",
            "--server.enableCORS=False",
        ]
    )
