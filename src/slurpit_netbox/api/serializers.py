from core.choices import DataSourceStatusChoices
from netbox.api.fields import ChoiceField
from netbox.api.serializers import NetBoxModelSerializer
from rest_framework import serializers
from netbox.api.serializers import WritableNestedSerializer

from slurpit_netbox.models import SlurpitPlanning, SlurpitImportedDevice, SlurpitStagedDevice, SlurpitLog, SlurpitSetting, SlurpitSnapshot, SlurpitMapping, SlurpitInitIPAddress, SlurpitInterface, SlurpitPrefix, SlurpitVLAN

__all__ = (
    'SlurpitPlanningSerializer',
    'SlurpitStagedDeviceSerializer',
    'SlurpitImportedDeviceSerializer',
    'SlurpitLogSerializer',
    'SlurpitSettingSerializer',
    'SlurpitSnapshotSerializer',
    'SlurpitInitIPAddressSerializer',
    'SlurpitInterfaceSerializer',
    'SlurpitPrefixSerializer'
)

class SlurpitPlanningSerializer(NetBoxModelSerializer):
    id = serializers.IntegerField(source='planning_id')
    comment = serializers.CharField(source='comments')

    class Meta:
        model = SlurpitPlanning
        fields = ['id', "name", "comment", "display"]

class SlurpitStagedDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlurpitStagedDevice
        fields = ['id', 'disabled', 'hostname', 'fqdn', 'ipv4', 'device_os', 'device_type', 'brand', 'createddate', 'changeddate']

class SlurpitInitIPAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlurpitInitIPAddress
        
        fields = [
            'id', 'url', 'display_url', 'display', 'family', 'address', 'vrf', 'tenant', 'status', 'role',
            'assigned_object_type', 'assigned_object_id', 'assigned_object', 'nat_inside', 'nat_outside',
            'dns_name', 'description', 'comments', 'tags', 'custom_fields', 'created', 'last_updated',
        ]

class SlurpitInterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlurpitInterface
        fields = [
            'id', 'url', 'display_url', 'display', 'device', 'vdcs', 'module', 'name', 'label', 'type', 'enabled',
            'parent', 'bridge', 'lag', 'mtu', 'mac_address', 'speed', 'duplex', 'wwn', 'mgmt_only', 'description',
            'mode', 'rf_role', 'rf_channel', 'poe_mode', 'poe_type', 'rf_channel_frequency', 'rf_channel_width',
            'tx_power', 'untagged_vlan', 'tagged_vlans', 'mark_connected', 'cable', 'cable_end', 'wireless_link',
            'link_peers', 'link_peers_type', 'wireless_lans', 'vrf', 'l2vpn_termination', 'connected_endpoints',
            'connected_endpoints_type', 'connected_endpoints_reachable', 'tags', 'custom_fields', 'created',
            'last_updated', 'count_ipaddresses', 'count_fhrp_groups', '_occupied',
        ]

class SlurpitSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlurpitSnapshot
        fields =  [ 'id', 'hostname', 'planning_id', 'content', 'result_type']


class SlurpitImportedDeviceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='slurpit_id')
    class Meta:
        model = SlurpitImportedDevice
        fields = ['id', 'disabled', 'hostname', 'fqdn', 'ipv4', 'device_os', 'device_type', 'brand', 'createddate', 'changeddate']

class SlurpitLogSerializer(NetBoxModelSerializer):
    class Meta:
        model = SlurpitLog
        fields = ['id', 'log_time', 'level', 'category', 'message']

class SlurpitSettingSerializer(WritableNestedSerializer):
    class Meta:
        model = SlurpitSetting
        fields = [ 'id', 'server_url', 'api_key', 'last_synced', 'connection_status', 'push_api_key', 'appliance_type']

class SlurpitMappingSerializer(NetBoxModelSerializer):
    class Meta:
        model = SlurpitMapping
        fields = [ 'id', 'source_field', 'target_field']

class SlurpitVLANSerializer(NetBoxModelSerializer):
    class Meta:
        model = SlurpitVLAN
        fields = [
            'id', 'url', 'display_url', 'display', 'site', 'group', 'vid', 'name', 'tenant', 'status', 'role',
            'description', 'comments', 'l2vpn_termination', 'tags', 'custom_fields', 'created', 'last_updated',
            'prefix_count',
        ]

class SlurpitPrefixSerializer(NetBoxModelSerializer):
    class Meta:
        model = SlurpitPrefix
        fields = [
            'id', 'url', 'display_url', 'display', 'family', 'prefix', 'site', 'vrf', 'tenant', 'vlan', 'status',
            'role', 'is_pool', 'mark_utilized', 'description', 'comments', 'tags', 'custom_fields',
            'created', 'last_updated', 'children', '_depth',
        ]