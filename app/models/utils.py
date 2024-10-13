from app.models.models import Tour, BookedTour, db

def get_all_tours():
    return Tour.query.all()

def get_tour(tour_id):
    return Tour.query.get_or_404(tour_id)


def get_booked_tour(booked_tour_id):
    return BookedTour.query.get(booked_tour_id)