from app import create_app, db
from app.models import Mileage, Vehicle, Grease, OilChange, PreventativeMaintenance

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'Mileage': Mileage,
            'Vehicle': Vehicle,
            'Grease': Grease,
            'OilChange': OilChange,
            'PreventativeMaintenance': PreventativeMaintenance}