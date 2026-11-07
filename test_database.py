from app import create_app, db
from app.models import Application
from datetime import date

app = create_app()
with app.app_context():
    # Create a new application instance
    new_application = Application(
        company_name="Example Company",
        position="Software Engineer",
        location="New York, NY",
        status="Applied",
        date_applied=date(2026, 11, 7),
    )

    # Add the new application to the session and commit it to the database
    db.session.add(new_application)
    db.session.commit()
    applications = Application.query.all()
    print (f"Added new application: {new_application.company_name} for position {new_application.position}")
    for application in applications:
        print(f"Application ID: {application.id}, Company: {application.company_name}, Position: {application.position}, Status: {application.status}, Date Applied: {application.date_applied}")
    applied_applications = Application.query.filter_by(status= "Applied").all()
    for application in applied_applications:
        print(f"Applied Application ID: {application.id}, Company: {application.company_name}, Position: {application.position}, Status: {application.status}, Date Applied: {application.date_applied}")
    application = db.session.get(Application, 1)
    application.status = "Interview"
    db.session.commit()