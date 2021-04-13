def init_foc_on_platform(foc):
    # CLASS FOR REGISTER MAPPING

    # REGISTERS ADDRESSING FOC
    # CONTROL
    registers = dict()  # map of registers. Every value of a key is a map with reg_address, reset_mode, rpm_mode, torque_mode
    registers["foc_ctrl_reg"] = dict()
    registers["foc_ctrl_reg"]["physical_address"] = foc.ip_dict["foc_0"][
        "phys_addr"]  # hex or not hex? base foc address
    registers["foc_ctrl_reg"]["address_range"] = foc.ip_dict["foc_0"]["addr_range"]
    registers["foc_ctrl_reg"]["control_registers"] = dict()
    registers["foc_ctrl_reg"]["control_registers"]["base_ctrl_register_foc"] = \
    foc.ip_dict["foc_0"]["registers"]["Memory_cntr"]["address_offset"]  # where the first ctrl register starts
    registers["foc_ctrl_reg"]["control_registers"]["data_width_base_ctrl_register_foc"] = int(
        int(foc.ip_dict["foc_0"]["parameters"]["C_S_AXI_ARGS_DATA_WIDTH"]) / 8)  # register alignment
    registers["foc_ctrl_reg"]["control_registers"]["number_of_registers_ctrl_foc"] = int(
        foc.ip_dict["foc_0"]["registers"]["Memory_cntr"]["size"] / registers["foc_ctrl_reg"]["control_registers"][
            "data_width_base_ctrl_register_foc"])  # number of register based on alignment value
    # STATUS
    registers["foc_ctrl_reg"]["status_registers"] = dict()
    registers["foc_ctrl_reg"]["status_registers"]["base_status_ctrl_register_foc"] = \
    foc.ip_dict["foc_0"]["registers"]["Memory_status"]["address_offset"]
    registers["foc_ctrl_reg"]["status_registers"]["data_width_base_status_ctrl_register_foc"] = int(
        int(foc.ip_dict["foc_0"]["parameters"]["C_S_AXI_ARGS_DATA_WIDTH"]) / 8)
    registers["foc_ctrl_reg"]["status_registers"]["number_of_registers_status_foc"] = int(
        foc.ip_dict["foc_0"]["registers"]["Memory_status"]["size"] / registers["foc_ctrl_reg"]["status_registers"][
            "data_width_base_status_ctrl_register_foc"])

    # REGISTER VALUES
    # WR 0
    registers["foc_ctrl_reg"]["control_registers"]["CONTROL"] = dict()
    registers["foc_ctrl_reg"]["control_registers"]["CONTROL"]["offset"] = \
    registers["foc_ctrl_reg"]["control_registers"]["base_ctrl_register_foc"] + \
    registers["foc_ctrl_reg"]["control_registers"]["data_width_base_ctrl_register_foc"] * 0
    registers["foc_ctrl_reg"]["control_registers"]["CONTROL"]["reset_mode"] = 0x0
    registers["foc_ctrl_reg"]["control_registers"]["CONTROL"]["rpm_mode"] = 0x141
    registers["foc_ctrl_reg"]["control_registers"]["CONTROL"]["torque_mode"] = 0x145
    # WR 1
    registers["foc_ctrl_reg"]["control_registers"]["FLUX_SP"] = dict()
    registers["foc_ctrl_reg"]["control_registers"]["FLUX_SP"]["offset"] = \
    registers["foc_ctrl_reg"]["control_registers"]["base_ctrl_register_foc"] + \
    registers["foc_ctrl_reg"]["control_registers"]["data_width_base_ctrl_register_foc"] * 1
    registers["foc_ctrl_reg"]["control_registers"]["FLUX_SP"]["reset_mode"] = 0x0
    registers["foc_ctrl_reg"]["control_registers"]["FLUX_SP"]["rpm_mode"] = 0x0
    registers["foc_ctrl_reg"]["control_registers"]["FLUX_SP"]["torque_mode"] = 0x0
    # WR 2
    registers["foc_ctrl_reg"]["control_registers"]["FLUX_KP"] = dict()
    registers["foc_ctrl_reg"]["control_registers"]["FLUX_KP"]["offset"] = \
    registers["foc_ctrl_reg"]["control_registers"]["base_ctrl_register_foc"] + \
    registers["foc_ctrl_reg"]["control_registers"]["data_width_base_ctrl_register_foc"] * 2
    registers["foc_ctrl_reg"]["control_registers"]["FLUX_KP"]["reset_mode"] = 0xFFFFF000
    registers["foc_ctrl_reg"]["control_registers"]["FLUX_KP"]["rpm_mode"] = 0xFFFFF000
    registers["foc_ctrl_reg"]["control_registers"]["FLUX_KP"]["torque_mode"] = 0xFFFFF000
    # WR 3
    registers["foc_ctrl_reg"]["control_registers"]["FLUX_KI"] = dict()
    registers["foc_ctrl_reg"]["control_registers"]["FLUX_KI"]["offset"] = \
    registers["foc_ctrl_reg"]["control_registers"]["base_ctrl_register_foc"] + \
    registers["foc_ctrl_reg"]["control_registers"]["data_width_base_ctrl_register_foc"] * 3
    registers["foc_ctrl_reg"]["control_registers"]["FLUX_KI"]["reset_mode"] = 0x0
    registers["foc_ctrl_reg"]["control_registers"]["FLUX_KI"]["rpm_mode"] = 0x0
    registers["foc_ctrl_reg"]["control_registers"]["FLUX_KI"]["torque_mode"] = 0x0
    # WR 4
    registers["foc_ctrl_reg"]["control_registers"]["TORQUE_SP"] = dict()
    registers["foc_ctrl_reg"]["control_registers"]["TORQUE_SP"]["offset"] = \
    registers["foc_ctrl_reg"]["control_registers"]["base_ctrl_register_foc"] + \
    registers["foc_ctrl_reg"]["control_registers"]["data_width_base_ctrl_register_foc"] * 4
    registers["foc_ctrl_reg"]["control_registers"]["TORQUE_SP"]["reset_mode"] = 0x0
    registers["foc_ctrl_reg"]["control_registers"]["TORQUE_SP"]["rpm_mode"] = 0x0
    registers["foc_ctrl_reg"]["control_registers"]["TORQUE_SP"]["torque_mode"] = 0x0
    # WR 5
    registers["foc_ctrl_reg"]["control_registers"]["TORQUE_KP"] = dict()
    registers["foc_ctrl_reg"]["control_registers"]["TORQUE_KP"]["offset"] = \
    registers["foc_ctrl_reg"]["control_registers"]["base_ctrl_register_foc"] + \
    registers["foc_ctrl_reg"]["control_registers"]["data_width_base_ctrl_register_foc"] * 5
    registers["foc_ctrl_reg"]["control_registers"]["TORQUE_KP"]["reset_mode"] = 0x1388
    registers["foc_ctrl_reg"]["control_registers"]["TORQUE_KP"]["rpm_mode"] = 0x1388
    registers["foc_ctrl_reg"]["control_registers"]["TORQUE_KP"]["torque_mode"] = 0xFFFFB1E0
    # WR 6
    registers["foc_ctrl_reg"]["control_registers"]["TORQUE_KI"] = dict()
    registers["foc_ctrl_reg"]["control_registers"]["TORQUE_KI"]["offset"] = \
    registers["foc_ctrl_reg"]["control_registers"]["base_ctrl_register_foc"] + \
    registers["foc_ctrl_reg"]["control_registers"]["data_width_base_ctrl_register_foc"] * 6
    registers["foc_ctrl_reg"]["control_registers"]["TORQUE_KI"]["reset_mode"] = 0x0
    registers["foc_ctrl_reg"]["control_registers"]["TORQUE_KI"]["rpm_mode"] = 0x0
    registers["foc_ctrl_reg"]["control_registers"]["TORQUE_KI"]["torque_mode"] = 0xFFFFEC78
    # WR 7
    registers["foc_ctrl_reg"]["control_registers"]["RPM_SP"] = dict()
    registers["foc_ctrl_reg"]["control_registers"]["RPM_SP"]["offset"] = registers["foc_ctrl_reg"]["control_registers"][
                                                                             "base_ctrl_register_foc"] + \
                                                                         registers["foc_ctrl_reg"]["control_registers"][
                                                                             "data_width_base_ctrl_register_foc"] * 7
    registers["foc_ctrl_reg"]["control_registers"]["RPM_SP"]["reset_mode"] = 0x0
    registers["foc_ctrl_reg"]["control_registers"]["RPM_SP"]["rpm_mode"] = 0x0
    registers["foc_ctrl_reg"]["control_registers"]["RPM_SP"]["torque_mode"] = 0x64
    # WR 8
    registers["foc_ctrl_reg"]["control_registers"]["RPM_KP"] = dict()
    registers["foc_ctrl_reg"]["control_registers"]["RPM_KP"]["offset"] = registers["foc_ctrl_reg"]["control_registers"][
                                                                             "base_ctrl_register_foc"] + \
                                                                         registers["foc_ctrl_reg"]["control_registers"][
                                                                             "data_width_base_ctrl_register_foc"] * 8
    registers["foc_ctrl_reg"]["control_registers"]["RPM_KP"]["reset_mode"] = 0xFFFFFF38
    registers["foc_ctrl_reg"]["control_registers"]["RPM_KP"]["rpm_mode"] = 0xFFFFFF38
    registers["foc_ctrl_reg"]["control_registers"]["RPM_KP"]["torque_mode"] = 0xFFFFFF38
    # WR 9
    registers["foc_ctrl_reg"]["control_registers"]["RPM_KI"] = dict()
    registers["foc_ctrl_reg"]["control_registers"]["RPM_KI"]["offset"] = registers["foc_ctrl_reg"]["control_registers"][
                                                                             "base_ctrl_register_foc"] + \
                                                                         registers["foc_ctrl_reg"]["control_registers"][
                                                                             "data_width_base_ctrl_register_foc"] * 9
    registers["foc_ctrl_reg"]["control_registers"]["RPM_KI"]["reset_mode"] = 0xFFFFFFFB
    registers["foc_ctrl_reg"]["control_registers"]["RPM_KI"]["rpm_mode"] = 0xFFFFFFFB
    registers["foc_ctrl_reg"]["control_registers"]["RPM_KI"]["torque_mode"] = 0xFFFFFFFB
    # WR 10
    registers["foc_ctrl_reg"]["control_registers"]["SHIFT"] = dict()
    registers["foc_ctrl_reg"]["control_registers"]["SHIFT"]["offset"] = registers["foc_ctrl_reg"]["control_registers"][
                                                                            "base_ctrl_register_foc"] + \
                                                                        registers["foc_ctrl_reg"]["control_registers"][
                                                                            "data_width_base_ctrl_register_foc"] * 10
    registers["foc_ctrl_reg"]["control_registers"]["SHIFT"]["reset_mode"] = 0x357
    registers["foc_ctrl_reg"]["control_registers"]["SHIFT"]["rpm_mode"] = 0x357
    registers["foc_ctrl_reg"]["control_registers"]["SHIFT"]["torque_mode"] = 0x164
    # WR 11
    registers["foc_ctrl_reg"]["control_registers"]["VD"] = dict()
    registers["foc_ctrl_reg"]["control_registers"]["VD"]["offset"] = registers["foc_ctrl_reg"]["control_registers"][
                                                                         "base_ctrl_register_foc"] + \
                                                                     registers["foc_ctrl_reg"]["control_registers"][
                                                                         "data_width_base_ctrl_register_foc"] * 11
    registers["foc_ctrl_reg"]["control_registers"]["VD"]["reset_mode"] = 0xFFFFE300
    registers["foc_ctrl_reg"]["control_registers"]["VD"]["rpm_mode"] = 0xFFFFE300
    registers["foc_ctrl_reg"]["control_registers"]["VD"]["torque_mode"] = 0xFFFFE300
    # WR 12
    registers["foc_ctrl_reg"]["control_registers"]["VQ"] = dict()
    registers["foc_ctrl_reg"]["control_registers"]["VQ"]["offset"] = registers["foc_ctrl_reg"]["control_registers"][
                                                                         "base_ctrl_register_foc"] + \
                                                                     registers["foc_ctrl_reg"]["control_registers"][
                                                                         "data_width_base_ctrl_register_foc"] * 12
    registers["foc_ctrl_reg"]["control_registers"]["VQ"]["reset_mode"] = 0xFFFFC100
    registers["foc_ctrl_reg"]["control_registers"]["VQ"]["rpm_mode"] = 0xFFFFC100
    registers["foc_ctrl_reg"]["control_registers"]["VQ"]["torque_mode"] = 0xFFFFC100
    # WR 13
    registers["foc_ctrl_reg"]["control_registers"]["FA"] = dict()
    registers["foc_ctrl_reg"]["control_registers"]["FA"]["offset"] = registers["foc_ctrl_reg"]["control_registers"][
                                                                         "base_ctrl_register_foc"] + \
                                                                     registers["foc_ctrl_reg"]["control_registers"][
                                                                         "data_width_base_ctrl_register_foc"] * 13
    registers["foc_ctrl_reg"]["control_registers"]["FA"]["reset_mode"] = 0
    registers["foc_ctrl_reg"]["control_registers"]["FA"]["rpm_mode"] = 0
    registers["foc_ctrl_reg"]["control_registers"]["FA"]["torque_mode"] = 18120
    # WR 14
    registers["foc_ctrl_reg"]["control_registers"]["FB"] = dict()
    registers["foc_ctrl_reg"]["control_registers"]["FB"]["offset"] = registers["foc_ctrl_reg"]["control_registers"][
                                                                         "base_ctrl_register_foc"] + \
                                                                     registers["foc_ctrl_reg"]["control_registers"][
                                                                         "data_width_base_ctrl_register_foc"] * 14
    registers["foc_ctrl_reg"]["control_registers"]["FB"]["reset_mode"] = 0
    registers["foc_ctrl_reg"]["control_registers"]["FB"]["rpm_mode"] = 0
    registers["foc_ctrl_reg"]["control_registers"]["FB"]["torque_mode"] = 14647
    # WR 15
    registers["foc_ctrl_reg"]["control_registers"]["CONTROL_REG2"] = dict()
    registers["foc_ctrl_reg"]["control_registers"]["CONTROL_REG2"]["offset"] = \
    registers["foc_ctrl_reg"]["control_registers"]["base_ctrl_register_foc"] + \
    registers["foc_ctrl_reg"]["control_registers"]["data_width_base_ctrl_register_foc"] * 15
    registers["foc_ctrl_reg"]["control_registers"]["CONTROL_REG2"]["reset_mode"] = 0x0
    registers["foc_ctrl_reg"]["control_registers"]["CONTROL_REG2"]["rpm_mode"] = 0x0
    registers["foc_ctrl_reg"]["control_registers"]["CONTROL_REG2"]["torque_mode"] = 0x100000

    # STATUS
    registers["foc_ctrl_reg"]["status_registers"]["ANGLE"] = dict()
    registers["foc_ctrl_reg"]["status_registers"]["ANGLE"]["offset"] = registers["foc_ctrl_reg"]["status_registers"][
                                                                           "base_status_ctrl_register_foc"] + \
                                                                       registers["foc_ctrl_reg"]["status_registers"][
                                                                           "data_width_base_status_ctrl_register_foc"] * 0

    registers["foc_ctrl_reg"]["status_registers"]["SPEED"] = dict()
    registers["foc_ctrl_reg"]["status_registers"]["SPEED"]["offset"] = registers["foc_ctrl_reg"]["status_registers"][
                                                                           "base_status_ctrl_register_foc"] + \
                                                                       registers["foc_ctrl_reg"]["status_registers"][
                                                                           "data_width_base_status_ctrl_register_foc"] * 1

    registers["foc_ctrl_reg"]["status_registers"]["ID"] = dict()
    registers["foc_ctrl_reg"]["status_registers"]["ID"]["offset"] = registers["foc_ctrl_reg"]["status_registers"][
                                                                        "base_status_ctrl_register_foc"] + \
                                                                    registers["foc_ctrl_reg"]["status_registers"][
                                                                        "data_width_base_status_ctrl_register_foc"] * 2

    registers["foc_ctrl_reg"]["status_registers"]["IQ"] = dict()
    registers["foc_ctrl_reg"]["status_registers"]["IQ"]["offset"] = registers["foc_ctrl_reg"]["status_registers"][
                                                                        "base_status_ctrl_register_foc"] + \
                                                                    registers["foc_ctrl_reg"]["status_registers"][
                                                                        "data_width_base_status_ctrl_register_foc"] * 3

    # REGISTER DATA STREAM ADDRESSING
    registers["capture_stream_data"] = dict()
    registers["capture_stream_data"]["physical_address"] = foc.ip_dict["AXI_StreamCapture_0"]["phys_addr"]
    registers["capture_stream_data"]["address_range"] = foc.ip_dict["AXI_StreamCapture_0"]["addr_range"]

    # REGISTER DATA STREAM MODES
    registers["capture_stream_data"]["modes"] = dict()
    registers["capture_stream_data"]["modes"]["CAPTURE_IA_IB_ANGLE_RPM"] = 0x0
    registers["capture_stream_data"]["modes"]["CAPTURE_ID_IQ"] = 0x2
    registers["capture_stream_data"]["modes"]["CAPTURE_VD_VQ"] = 0x6

    return registers
