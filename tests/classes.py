# код, в котором в объявлены все классы 
from dataclasses import *
from dataclasses_json import *

# LOGIN
@dataclass_json
@dataclass
class Login:
	login: str
	password: str


@dataclass_json
@dataclass
class Update_Login:
	login: str
	email: str

# l = Login("dhgdflgj", "dfghdghdf")

#  USER
@dataclass_json
@dataclass
class User:
	company: str
	login: str
	email: str
	password: str
	rank: str

@dataclass_json
@dataclass
class Update_User:
	company: str
	login: str
	email: str
	rank: str


@dataclass_json
@dataclass
class New_Password:
	old_password: str
	password: str

# BPLA

@dataclass_json
@dataclass
class Bpla:
	bort_number: str
	encryption_key: str
	model: str
	modem_id: str
	type: int
	user_id: str


@dataclass_json
@dataclass
class Update_Bpla:
	encryption_key: str
	modem_id: str


# FLIGHT

@dataclass_json
@dataclass
class Waypoints:
	latitude: int
	longitude: int
	altitude: int
	airspeed: float
	groundspeed: float
	distance: float
	heading: int
	param1: float
	param2: float
	param3: float
	param: float
	svp_id: str
	can_switch_svp: bool
	switched_svp: bool
	svp_new_id: str
	unix_timestmp: int

@dataclass_json
@dataclass
class Flight:
	bpla_id: str
	waypoints: list[Waypoints]


# f = Flight("asd", Waypoints(10, 20, 30, 40.5, 50.5, 60.5, 70, 80.5, 90.5,100.5, 110.5,"svp_id_1", True,False, "svp_new_id_1", 123456789))
#
# print(f)
