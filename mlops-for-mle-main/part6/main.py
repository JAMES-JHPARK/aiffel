import threading
import subprocess

def run_streamlit():
    subprocess.run(["streamlit", "run", "streamlit.py"])

def run_fastapi():
    subprocess.run(["uvicorn", "app:app", "-reload"])

if __name__=='__main__':
    streamlit_thread = threading.Thread(target=run_streamlit)
    streamlit_thread.start()

    fastapi_thread = threading.Thread(target=run_fastapi)
    fastapi_thread.start()

    streamlit_thread.join()
    streamlit_thread.join()