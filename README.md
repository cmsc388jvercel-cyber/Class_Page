# CMSC388J Class Page

Flask app for the CMSC388J course page, set up to deploy on Vercel with zero config
beyond importing this repo (uses @vercel/python via vercel.json, routes everything
to app.py).

## Local dev setup

```
pip install -r requirements.txt
npm install -D @tailwindcss/typography
chmod +x tw.sh
```

Then, in two terminal tabs:
```
./tw.sh              # watches templates, rebuilds static/custom.css
flask run --debug    # dev server, picks up template changes
```

## Deploying on Vercel

1. Push this repo to GitHub.
2. In Vercel, "Add New Project" -> import the repo. No build settings needed;
   vercel.json handles it.
3. Once deployed, rename the Vercel project (Settings -> General) if you want a
   cleaner *.vercel.app URL instead of an auto-generated one.

Routes are defined in app.py: `/` redirects to `/388j` (homepage), `/388j/projects`
is the projects page. Edit `templates/homepage/schedule.html` for the weekly schedule.
