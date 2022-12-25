from typing import Any

from django.contrib.gis.gdal.base import GDALBase as GDALBase
from django.contrib.gis.gdal.field import Field as Field
from django.contrib.gis.gdal.geometries import OGRGeometry as OGRGeometry
from django.contrib.gis.gdal.geomtype import OGRGeomType as OGRGeomType

class Feature(GDALBase):
    destructor: Any
    ptr: Any
    def __init__(self, feat: Any, layer: Any) -> None: ...
    def __getitem__(self, index: str | int) -> Field: ...
    def __len__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    @property
    def encoding(self) -> str: ...
    @property
    def fid(self) -> int: ...
    @property
    def layer_name(self) -> str: ...
    @property
    def num_fields(self) -> int: ...
    @property
    def fields(self) -> list[str]: ...
    @property
    def geom(self) -> OGRGeometry: ...
    @property
    def geom_type(self) -> OGRGeomType: ...
    def get(self, field: str) -> Any: ...
    def index(self, field_name: str) -> Any: ...
