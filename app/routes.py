from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    items=[
        {"title": "Small Group Tours", "description": "Travel with a small group of like-minded people and enjoy the safety and security of travelling with an experienced guide.", "price": "From $1,000", "image": "https://images.unsplash.com/photo-1592921870789-04563d55041c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80"},
        {"title": "Private Tours", "description": "Travel with a small group of like-minded people and enjoy the safety and security of travelling with an experienced guide.", "price": "From $1,000", "image": "https://images.unsplash.com/photo-1592921870789-04563d55041c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80"},
        {"title": "Tailor-Made Tours", "description": "Travel with a small group of like-minded people and enjoy the safety and security of travelling with an experienced guide.", "price": "From $1,000", "image": "https://images.unsplash.com/photo-1592921870789-04563d55041c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80"},
    ]
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/destinations')
def locations():
    return render_template('destinations.html')

@main.route('/register')
def register():
    return render_template('register.html')

@main.route('/packages')
def packages():
    return render_template('packages.html')

@main.route('/accomodation')
def accomodation():
    return render_template('accomodation.html')

@main.route('/enquire-now')
def enquire():
    return render_template('enquire-now.html')
