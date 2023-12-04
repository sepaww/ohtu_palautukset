




class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if  matcher.test(player):
                return True
        return False
class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value
    
class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class Not:
    def __init__(self, rule):
        self._rule=rule

    def test(self, player):
        return not self._rule.test(player)
    
class All:
    def __init__(self):
        pass

    def test(self, player):
       return 1 

class QueryBuilder:
    def __init__(self, rules=[], rule=0, typer=And):
        self._rules=rules
        #self._rule=rule
        self._typer=typer
        if rule:
            self._rules.append(rule)

    def hasAtLeast(self, val, attr):
        return QueryBuilder(self._rules, HasAtLeast(val, attr), self._typer)

    def playsIn(self, team):
        return QueryBuilder(self._rules, PlaysIn(team), self._typer)
    
    def build(self):
        cope_copy=self._rules[:]
        self._rules.clear()
        if len(cope_copy)>0:
            return self._typer(*cope_copy)
        else:
            return All()
    
    def hasFewerThan(self, val, attr):
        return QueryBuilder(self._rules, HasFewerThan(val, attr), self._typer)
    
    #def oneOf(self, *rules):
    ##    for rule in rules:
     #       self._rules.append(rule)
    #    return QueryBuilder(self._rules, 0, Or)

    def oneOf(self, *rules):
        return QueryBuilder([*rules], 0, Or)