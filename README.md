Push a prototype model.pkl (make sure its named model.pkl)
Ensure the fields match those of app.py
This repo is tied to a render.com service called ENG2112 (https://eng2112.onrender.com)
If the render.com service hasn't been queried for a while it stops and takes ~30 seconds to boot again (not a biggie but worth considering for a presentation)
Check if the render.com service is healthy by querying https://eng2112.onrender.com/health
/health returning status OK means the service is reachable, not that the service actually works
The UI itself is running off a single HTML which I'm pushing directly to Cloudflare (my domain registrar)
index.html takes the inputs (these can be adjusted), packages them and sends them to the render.com service which runs the model then sends this back to the webpage
Notes:
index.html, app.py and requirements.txt are all straight out of Claude.
