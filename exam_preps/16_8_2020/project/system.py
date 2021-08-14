from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware


class System:

    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware = hardware[0]
        try:
            hardware.install(express_software)
            System._software.append(express_software)
        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware = hardware[0]
        try:
            hardware.install(light_software)
            System._software.append(light_software)
        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        software = [s for s in System._software if s.name == software_name]
        if not hardware or not software:
            return "Some of the components do not exist"
        hardware = hardware[0]
        software = software[0]
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        hardware_components = len(System._hardware)
        software_components = len(System._software)
        total_used_memory = sum([s.memory_consumption for s in System._software])
        total_memory = sum([h.memory for h in System._hardware])
        total_used_space = sum([s.capacity_consumption for s in System._software])
        total_space = sum([h.capacity for h in System._hardware])
        string_to_return = f"System Analysis\nHardware Components: {hardware_components}\n" \
                           f"Software Components: {software_components}\n" \
                           f"Total Operational Memory: {total_used_memory} / {total_memory}\n" \
                           f"Total Capacity Taken: {total_used_space} / {total_space}"
        return string_to_return

    @staticmethod
    def system_split():
        string_to_return = ""
        for hardware in System._hardware:
            express_software = [es for es in hardware.software_components if es.type == "Express"]
            light_software = [ls for ls in hardware.software_components if ls.type == "Light"]
            memory_used = sum([s.memory_consumption for s in hardware.software_components])
            capacity_used = sum([s.capacity_consumption for s in hardware.software_components])
            software_names = [s.name for s in hardware.software_components]
            hardware_type = hardware.__class__.__name__[:-8]
            string_to_return += f"Hardware Component - {hardware.name}\n" \
                                f"Express Software Components: {len(express_software)}\n" \
                                f"Light Software Components: {len(light_software)}\n" \
                                f"Memory Usage: {memory_used} / {hardware.memory}\n" \
                                f"Capacity Usage: {capacity_used} / {hardware.capacity}\n" \
                                f"Type: {hardware_type}\n"
            if not software_names:
                string_to_return += "Software Components: None"
            else:
                string_to_return += f"Software Components: {', '.join(software_names)}"
        return string_to_return


# Hardware Component - {component name}
# Express Software Components: {number of the installed express software components}
# Light Software Components: {number of the installed light software components}
# Memory Usage: {total memory used of all installed software components} / {total memory of the hardware}
# Capacity Usage: {total capacity used of all installed software components } / {total capacity of the hardware}
# Type: {type}
# Software Components: {names of all software components separated by ', '} (or 'None' if no software components)
