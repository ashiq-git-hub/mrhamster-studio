@echo off
title Mr. Hamster Studio - Deploy to Production
echo ========================================================
echo   Mr. Hamster Studio - Permanent Production Deployment
echo ========================================================
echo.
echo 1. Rebuilding studio artifacts...
python scripts\build_website.py
echo.
echo 2. Pushing updates to GitHub (Triggers Vercel CI/CD)...
git add .
git commit -m "feat: Luxury Minimalist Swiss Atelier redesign, semantic HTML5, smooth mobile UX"
git push origin master
echo.
echo ========================================================
echo [SUCCESS] Pushed to GitHub repository!
echo Vercel automatically deploys to permanent domain:
echo.
echo   https://mrhamster-studio.vercel.app
echo.
echo ========================================================
pause
