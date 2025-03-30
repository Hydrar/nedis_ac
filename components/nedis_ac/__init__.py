import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

nedis_ac_ns = cg.esphome_ns.namespace("Nedis_AC")
NedisAC = nedis_ac_ns.class_("NedisAC", cg.Component)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(NedisAC),
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)