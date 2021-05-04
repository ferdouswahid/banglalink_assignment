### Run Task B
1. open cmd 
2. goto the directory of code till Task-B. Please change the path accordingly.

```bash 
cd /banglalink_assignment/set-1/Task-B
ls
```

3. install Flask

```bash 
pip3 install flask

Or

pip install flask
```

4. then run 
```bash
export FLASK_APP=Task_B.py

flask run --host 0.0.0.0 --port 4000

```

or

```
export FLASK_APP=Task_B.py
python3 -m flask run --host 0.0.0.0 --port 4000

or

export FLASK_APP=Task_B.py
python -m flask run --host 0.0.0.0 --port 4000
```

5. then call the url from browser or any http client to get response `http://localhost:4000/`

