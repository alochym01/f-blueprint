# Caller-ANI: 			18
# Caller-Context: 		default
# Caller-Destination-Number: 	0332124293
# Caller-Network-Addr: 		192.168.1.102
# FreeSWITCH-IPv4: 		192.168.1.10
# variable_local_media_port: 	27882
# Other-Type: 			originatee
# Channel-State: 			CS_REPORTING
# Event-Name: 			CHANNEL_HANGUP_COMPLETE
# Hangup-Cause: 			USER_BUSY
# Other-Leg-Destination-Number: 	0332124293
# Other-Leg-Network-Addr: 	192.168.1.22
# variable_remote_media_port: 	56945
# variable_bridge_epoch: 		1544442189
# variable_answer_epoch: 		0
# variable_answersec: 		0
# variable_billsec: 		0
# variable_duration: 		45
# variable_end_epoch: 		1544442233
# variable_rtp_use_codec_name: 	PCMU
# variable_rtp_use_codec_ptime: 	20
# variable_rtp_use_codec_rate: 	8000
# variable_rtp_audio_in_mos: 	4.50
# Core-UUID: 			cc91c00a-fb9b-11e8-b55a-bdfb7b7641bf
# Channel-Call-UUID: 		477126b1-0e9d-9b1e-f5e9-aaecb036934c
# variable_call_uuid: 		477126b1-0e9d-9b1e-f5e9-aaecb036934c
# variable_uuid: 			477126b1-0e9d-9b1e-f5e9-aaecb036934c
from app import db

class Cdr(db.Model):
    __tablename__ = 'cdrs'
    id = db.Column(db.Integer, primary_key=True)
    ani = db.Column(db.Integer, nullable=True)
    dnis = db.Column(db.Integer, nullable=True)
    context = db.Column(db.String(128), default="default")
    ani_addr = db.Column(db.String(120), nullable=True)
    server_addr = db.Column(db.String(120), default="192.168.1.10")
    v_local_media_port = db.Column(db.Integer, nullable=True)
    other_type = db.Column(db.String(120), nullable=True)
    caller_rdnis = db.Column(db.Integer, nullable=True)
    event_name = db.Column(db.String(120), nullable=True)
    channel_state = db.Column(db.String(120), nullable=True)
    hangup_cause = db.Column(db.String(120), nullable=True)
    dnis_addr = db.Column(db.String(120), nullable=True)
    v_remote_media_port = db.Column(db.Integer, nullable=True)
    v_bridge_epoch = db.Column(db.Integer, nullable=True)
    v_answer_epoch = db.Column(db.Integer, nullable=True)
    v_answersec = db.Column(db.Integer, nullable=True)
    v_billsec = db.Column(db.Integer, nullable=True)
    v_duration = db.Column(db.Integer, nullable=True)
    v_end_epoch = db.Column(db.Integer, nullable=True)
    v_codec = db.Column(db.String(120), nullable=True)
    v_codec_ptime = db.Column(db.String(120), nullable=True)
    v_codec_rate = db.Column(db.String(120), nullable=True)
    v_mos = db.Column(db.String(120), nullable=True)
    core_uuid = db.Column(db.String(512), nullable=True)
    channel_call_uuid = db.Column(db.String(512), nullable=True)
    v_call_uuid = db.Column(db.String(512), nullable=True)
    v_uuid = db.Column(db.String(512), nullable=True)

    def __repr__(self):
        return f"Caller {self.ani} call to {self.dnis} with duration {self.v_duration} and bill {self.v_billsec}"
