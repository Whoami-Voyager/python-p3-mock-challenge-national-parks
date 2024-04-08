class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if type(value) is str and len(value) >= 3 and not hasattr(self, 'name'):
            self._name = value
        else:
            print("not right name")
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitors = [trip.visitor for trip in self.trips()]
        return max(set(visitors), key=visitors.count)

    @classmethod
    def most_visited(cls):
        return max(cls.all, key=lambda park: park.total_visits())

class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self, value):
        if type(value) is str and len(value) >= 7:
            self._start_date = value
        else:
            print("not valid start date")

    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self, value):
        if type(value) is str and len(value) >= 7:
            self._end_date = value
        else:
            print("not valid end date")


    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor

    def national_park(self):
        park_list = []
        for park in Trip.all:
            if park.national_park is self:
                park_list.append(self)
        return park_list

    @property
    def national_park(self):
        return self._national_park
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park

class Visitor:

    all = []

    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            print("not right name")

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    def total_visits_at_park(self, park):
        if not park.visitors():
            return len([trip for trip in self.trips() if trip.national_park is self])
