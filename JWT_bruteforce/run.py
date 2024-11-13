from flask import Flask, render_template, flash, redirect, url_for
from application import app

if __name__ == "__main__":
    app.run(debug=True)
