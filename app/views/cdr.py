from flask import Blueprint, request, jsonify,render_template, current_app, url_for
from app import db
from app.models.cdr import Cdr
import json

cdr = Blueprint('cdr', __name__)

@cdr.route('/')
def cdr_index():
    page = request.args.get('page', 1, type=int)
    cdrs = Cdr.query.paginate(page, current_app.config['ITEMS_PER_PAGE'], False)
    return render_template("cdr/index.html", cdrs=cdrs)

@cdr.route('/create', methods=['POST'])
def cdr_create():
    vals = request.get_json()
    cdr = Cdr(
            ani = vals["Caller-ANI"],
            context = vals["Caller-Context"],
            dnis = vals["Caller-Destination-Number"],
            ani_addr = vals["Caller-Network-Addr"],
            server_addr = vals["FreeSWITCH-IPv4"],
            v_local_media_port = vals["variable_local_media_port"],
            other_type = vals["Other-Type"],
            caller_rdnis = vals["Caller-RDNIS"],
            channel_state = vals["Channel-State"],
            event_name = vals["Event-Name"],
            hangup_cause = vals["Hangup-Cause"],
            dnis_addr = vals["Other-Leg-Network-Addr"],
            v_remote_media_port = vals["variable_remote_media_port"],
            v_bridge_epoch = vals["variable_bridge_epoch"],
            v_answer_epoch = vals["variable_answer_epoch"],
            v_answersec = vals["variable_answersec"],
            v_billsec = vals["variable_billsec"],
            v_duration = vals["variable_duration"],
            v_end_epoch = vals["variable_end_epoch"],
            v_codec = vals["variable_rtp_use_codec_name"],
            v_codec_ptime = vals["variable_rtp_use_codec_ptime"],
            v_codec_rate = vals["variable_rtp_use_codec_rate"],
            v_mos = vals["variable_rtp_audio_in_mos"],
            core_uuid = vals["Core-UUID"],
            channel_call_uuid = vals["Channel-Call-UUID"],
            v_call_uuid = vals["variable_call_uuid"],
            v_uuid = vals["variable_uuid"]
        )
    db.session.add(cdr)
    db.session.commit()

    return jsonify(str(cdr))