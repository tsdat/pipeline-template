from pathlib import Path

from pydantic import Extra, Field
from tsdat import (
    DatasetConfig,
    PipelineConfig,
    QualityConfig,
    RetrieverConfig,
    StorageConfig,
)
from tsdat.config.attributes import GlobalAttributes


class ACDDGlobalAttrs(GlobalAttributes, extra=Extra.allow):
    id: str = Field(
        ...,
        regex=r".", 
        title="ID",
        description="An identifier for the data set, provided by and unique within its naming authority. The combination of the 'naming_authority' and the 'id' should be globally unique, but the 'id' can be globally unique by itself also. IDs can be URLs, URNs, DOIs, meaningful text strings, a local key, or any other unique string of characters. The id should not include white space characters.",
    )
    naming_authority: str = Field(
        ...,
        regex=r".",
        title="Naming Authority",
        description="The organization that provides the initial id (see above) for the dataset. The naming authority should be uniquely specified by this attribute. We recommend using reverse-DNS naming for the naming authority; URIs are also acceptable. Example: 'edu.ucar.unidata'.",
    )
    source: str = Field(
        ...,
        regex=r".",
        title="Source",
        description="The method of production of the original data. If it was model-generated, source should name the model and its version. If it is observational, source should characterize it. Examples: 'temperature from CTD #1234'; 'world model v.0.1'.",
    )
    processing_level: str = Field(
        ...,
        regex=r".",
        title="Processing Level",
        description="A textual description of the processing (or quality control) level of the data.",
    )
    comment: str = Field(
        ...,
        regex=r".",
        title="Comment",
        description="Miscellaneous information about the data, not captured elsewhere.",
    )
    acknowledgement: str = Field(
        ...,
        regex=r".",
        title="Acknowledgement",
        description="A place to acknowledge various types of support for the project that produced this data.",
    )
    license: str = Field(
        ...,
        regex=r".",
        title="License",
        description="Provide the URL to a standard or specific license, enter 'Freely Distributed' or 'None', or describe any restrictions to data access and distribution in free text.",
    )
    standard_name_vocabulary: str = Field(
        ...,
        regex=r".",
        title="Standard Name Vocabulary",
        description="The name and version of the controlled vocabulary from which variable standard names are taken. Example: 'CF Standard Name Table v27'.",
    )
    date_created: str = Field(
        ...,
        regex=r".",
        title="Date Created",
        description="The date on which this version of the data was created. (Modification of values implies a new version, hence this would be assigned the date of the most recent values modification.) Metadata changes are not considered when assigning the date_created. The ISO 8601:2004 extended date format is recommended.",
    )
    creator_name: str = Field(
        ...,
        regex=r".",
        title="Creator Name",
        description="The name of the person (or other creator type specified by the creator_type attribute) principally responsible for creating this data.",
    )
    creator_email: str = Field(
        ...,
        regex=r".",
        title="Creator Email",
        description="The email address of the person (or other creator type specified by the creator_type attribute) principally responsible for creating this data.",
    )
    creator_url: str = Field(
        ...,
        regex=r".",
        title="Creator URL",
        description="The URL of the person (or other creator type specified by the creator_type attribute) principally responsible for creating this data.",
    )
    creator_type: str = Field(
        ...,
        regex=r".",
        title="Creator Type",
        description="Specifies type of creator with one of the following: 'person', 'group', 'institution', or 'position'. If this attribute is not specified, the creator is assumed to be a person.",
    )
    creator_institution: str = Field(
        ...,
        regex=r".",
        title="Creator Institution",
        description="The institution of the creator; should uniquely identify the creator's institution. This attribute's value should be specified even if it matches the value of publisher_institution, or if creator_type is institution.",
    )
    contributor_name: str = Field(
        ...,
        regex=r".",
        title="Contributor Name(s)",
        description="The name of any individuals, projects, or institutions that contributed to the creation of this data. May be presented as free text, or in a structured format compatible with conversion to ncML (e.g., insensitive to changes in whitespace, including end-of-line characters).",
    )
    contributor_role: str = Field(
        ...,
        regex=r".",
        title="Contributor Role(s)",
        description="The role of any individuals, projects, or institutions that contributed to the creation of this data. May be presented as free text, or in a structured format compatible with conversion to ncML (e.g., insensitive to changes in whitespace, including end-of-line characters). Multiple roles should be presented in the same order and number as the names in contributor_names.",
    )
    institution: str = Field(
        ...,
        regex=r".",
        title="Institution",
        description="The name of the institution principally responsible for originating this data.",
    )
    program: str = Field(
        ...,
        regex=r".",
        title="Program",
        description="The overarching program(s) of which the dataset is a part. A program consists of a set (or portfolio) of related and possibly interdependent projects that meet an overarching objective. Examples: 'GHRSST', 'NOAA CDR', 'NASA EOS', 'JPSS', 'GOES-R'.",
    )
    project: str = Field(
        ...,
        regex=r".",
        title="Project",
        description="The name of the project(s) principally responsible for originating this data. Multiple projects can be separated by commas, as described under Attribute Content Guidelines. Examples: 'PATMOS-X', 'Extended Continental Shelf Project'.",
    )
    publisher_name: str = Field(
        ...,
        regex=r".",
        title="Publisher Name",
        description="The name of the person (or other entity specified by the publisher_type attribute) responsible for publishing the data file or product to users, with its current metadata and format.",
    )
    publisher_email: str = Field(
        ...,
        regex=r".",
        title="Publisher Email",
        description="The email address of the person (or other entity specified by the publisher_type attribute) responsible for publishing the data file or product to users, with its current metadata and format.",
    )
    publisher_url: str = Field(
        ...,
        regex=r".",
        title="Publisher URL",
        description="The URL of the person (or other entity specified by the publisher_type attribute) responsible for publishing the data file or product to users, with its current metadata and format.",
    )
    publisher_type: str = Field(
        ...,
        regex=r".",
        title="Publisher Type",
        description="Specifies type of publisher with one of the following: 'person', 'group', 'institution', or 'position'. If this attribute is not specified, the publisher is assumed to be a person.",
    )
    publisher_institution: str = Field(
        ...,
        regex=r".",
        title="Publisher Institution",
        description="Specifies type of publisher with one of the following: 'person', 'group', 'institution', or 'position'. If this attribute is not specified, the publisher is assumed to be a person.",
    )
    geospatial_bounds: str = Field(
        ...,
        regex=r".",
        title="Geospatial Bounds",
        description="Describes the data's 2D or 3D geospatial extent in OGC's Well-Known Text (WKT) Geometry format (reference the OGC Simple Feature Access (SFA) specification). The meaning and order of values for each point's coordinates depends on the coordinate reference system (CRS). The ACDD default is 2D geometry in the EPSG:4326 coordinate reference system. The default may be overridden with geospatial_bounds_crs and geospatial_bounds_vertical_crs (see those attributes). EPSG:4326 coordinate values are latitude (decimal degrees_north) and longitude (decimal degrees_east), in that order. Longitude values in the default case are limited to the [-180, 180) range. Example: 'POLYGON ((40.26 -111.29, 41.26 -111.29, 41.26 -110.29, 40.26 -110.29, 40.26 -111.29))'.",
    )
    geospatial_bounds_crs: str = Field(
        ...,
        regex=r".",
        title="Geospatial Bounds Coordinate Reference System",
        description="The coordinate reference system (CRS) of the point coordinates in the geospatial_bounds attribute. This CRS may be 2-dimensional or 3-dimensional, but together with geospatial_bounds_vertical_crs, if that attribute is supplied, must match the dimensionality, order, and meaning of point coordinate values in the geospatial_bounds attribute. If geospatial_bounds_vertical_crs is also present then this attribute must only specify a 2D CRS. EPSG CRSs are strongly recommended. If this attribute is not specified, the CRS is assumed to be EPSG:4326. Examples: 'EPSG:4979' (the 3D WGS84 CRS), 'EPSG:4047'.",
    )
    geospatial_bounds_vertical_crs: str = Field(
        ...,
        regex=r".",
        title="Geospatial Bounds Vertical Coordinate Reference System",
        description="The vertical coordinate reference system (CRS) for the Z axis of the point coordinates in the geospatial_bounds attribute. This attribute cannot be used if the CRS in geospatial_bounds_crs is 3-dimensional; to use this attribute, geospatial_bounds_crs must exist and specify a 2D CRS. EPSG CRSs are strongly recommended. There is no default for this attribute when not specified. Examples: 'EPSG:5829' (instantaneous height above sea level), 'EPSG:5831' (instantaneous depth below sea level), or 'EPSG:5703' (NAVD88 height).",
    )
    geospatial_lat_min: float = Field(
        ...,
        regex=r".",
        title="Geospatial Latitude Minimum",
        description="Describes a simple lower latitude limit; may be part of a 2- or 3-dimensional bounding region. Geospatial_lat_min specifies the southernmost latitude covered by the dataset.",
    )
    geospatial_lat_max: float = Field(
        ...,
        regex=r".",
        title="Geospatial Latitude Maximum",
        description="Describes a simple upper latitude limit; may be part of a 2- or 3-dimensional bounding region. Geospatial_lat_max specifies the northernmost latitude covered by the dataset.",
    )
    geospatial_lon_min: float = Field(
        ...,
        regex=r".",
        title="Geospatial Longitude Minimum",
        description="Describes a simple longitude limit; may be part of a 2- or 3-dimensional bounding region. geospatial_lon_min specifies the westernmost longitude covered by the dataset. See also geospatial_lon_max.",
    )
    geospatial_lon_max: float = Field(
        ...,
        regex=r".",
        title="Geospatial Longitude Maximum",
        description="Describes a simple longitude limit; may be part of a 2- or 3-dimensional bounding region. geospatial_lon_max specifies the easternmost longitude covered by the dataset. Cases where geospatial_lon_min is greater than geospatial_lon_max indicate the bounding box extends from geospatial_lon_max, through the longitude range discontinuity meridian (either the antimeridian for -180:180 values, or Prime Meridian for 0:360 values), to geospatial_lon_min; for example, geospatial_lon_min=170 and geospatial_lon_max=-175 incorporates 15 degrees of longitude (ranges 170 to 180 and -180 to -175).",
    )
    geospatial_vertical_min: float = Field(
        ...,
        regex=r".",
        title="Geospatial Vertical Minimum",
        description="Describes the numerically smaller vertical limit; may be part of a 2- or 3-dimensional bounding region. See geospatial_vertical_positive and geospatial_vertical_units.",
    )
    geospatial_vertical_max: float = Field(
        ...,
        regex=r".",
        title="Geospatial Vertical Maximum",
        description="Describes the numerically larger vertical limit; may be part of a 2- or 3-dimensional bounding region. See geospatial_vertical_positive and geospatial_vertical_units.",
    )
    geospatial_vertical_positive: str = Field(
        ...,
        regex=r".",
        title="Geospatial Vertical Maximum",
        description="One of 'up' or 'down'. If up, vertical values are interpreted as 'altitude', with negative values corresponding to below the reference datum (e.g., under water). If down, vertical values are interpreted as 'depth', positive values correspond to below the reference datum. Note that if geospatial_vertical_positive is down ('depth' orientation), the geospatial_vertical_min attribute specifies the data's vertical location furthest from the earth's center, and the geospatial_vertical_max attribute specifies the location closest to the earth's center.",
    )
    geospatial_lat_units: str = Field(
        ...,
        regex=r".",
        title="Geospatial Latitude Units",
        description="Units for the latitude axis described in 'geospatial_lat_min' and 'geospatial_lat_max' attributes. These are presumed to be 'degree_north'; other options from udunits may be specified instead.",
    )
    geospatial_lat_resolution: str = Field(
        ...,
        regex=r".",
        title="Geospatial Latitude Resolution",
        description="Information about the targeted spacing of points in latitude. Recommend describing resolution as a number value followed by the units. Examples: '100 meters', '0.1 degree'.",
    )
    geospatial_lon_units: str = Field(
        ...,
        regex=r".",
        title="Geospatial Longitude Units",
        description="Units for the longitude axis described in 'geospatial_lon_min' and 'geospatial_lon_max' attributes. These are presumed to be 'degree_east'; other options from udunits may be specified instead.",
    )
    geospatial_lon_resolution: str = Field(
        ...,
        regex=r".",
        title="Geospatial Longitude Resolution",
        description="Information about the targeted spacing of points in longitude. Recommend describing resolution as a number value followed by units. Examples: '100 meters', '0.1 degree'.",
    )
    geospatial_vertical_units: str = Field(
        ...,
        regex=r".",
        title="Geospatial Vertical Units",
        description="Units for the vertical axis described in 'geospatial_vertical_min' and 'geospatial_vertical_max' attributes. The default is EPSG:4979 (height above the ellipsoid, in meters); other vertical coordinate reference systems may be specified. Note that the common oceanographic practice of using pressure for a vertical coordinate, while not strictly a depth, can be specified using the unit bar. Examples: 'EPSG:5829' (instantaneous height above sea level), 'EPSG:5831' (instantaneous depth below sea level).",
    )
    geospatial_vertical_resolution: str = Field(
        ...,
        regex=r".",
        title="Geospatial Vertical Resolution",
        description="Information about the targeted vertical spacing of points. Example: '25 meters'.",
    )
    time_coverage_start: str = Field(
        ...,
        regex=r".",
        title="Time Coverage Start",
        description="Describes the time of the first data point in the data set. Use the ISO 8601:2004 date format, preferably the extended format as recommended in the Attribute Content Guidance section.",
    )
    time_coverage_end: str = Field(
        ...,
        regex=r".",
        title="Time Coverage End",
        description="Describes the time of the last data point in the data set. Use ISO 8601:2004 date format, preferably the extended format as recommended in the Attribute Content Guidance section.",
    )
    time_coverage_duration: str = Field(
        ...,
        regex=r".",
        title="Time Coverage Duration",
        description="Describes the duration of the data set. Use ISO 8601:2004 duration format, preferably the extended format as recommended in the Attribute Content Guidance section.",
    )
    time_coverage_resolution: str = Field(
        ...,
        regex=r".",
        title="Time Coverage Resolution",
        description="Describes the targeted time period between each value in the data set. Use ISO 8601:2004 duration format, preferably the extended format as recommended in the Attribute Content Guidance section.",
    )
    date_modified: str = Field(
        ...,
        regex=r".",
        title="Date Modified",
        description="The date on which the data was last modified. Note that this applies just to the data, not the metadata. The ISO 8601:2004 extended date format is recommended.",
    )
    date_issued: str = Field(
        ...,
        regex=r".",
        title="Date Issued",
        description="The date on which this data (including all modifications) was formally issued (i.e., made available to a wider audience). Note that these apply just to the data, not the metadata. The ISO 8601:2004 extended date format is recommended.",
    )
    date_metadata_modified: str = Field(
        ...,
        regex=r".",
        title="Date Metadata Modified",
        description="The date on which the metadata was last modified. The ISO 8601:2004 extended date format is recommended.",
    )
    product_version: str = Field(
        ...,
        regex=r".",
        title="Product Version",
        description="Version identifier of the data file or product as assigned by the data creator. For example, a new algorithm or methodology could result in a new product_version.",
    )
    keywords: str = Field(
        ...,
        regex=r".",
        title="Keywords",
        description="A comma-separated list of key words and/or phrases. Keywords may be common words or phrases, terms from a controlled vocabulary (GCMD is often used), or URIs for terms from a controlled vocabulary (see also 'keywords_vocabulary' attribute.",
    )
    keywords_vocabulary: str = Field(
        ...,
        regex=r".",
        title="Keywords Vocabulary",
        description="If you are using a controlled vocabulary for the words/phrases in your 'keywords' attribute, this is the unique name or identifier of the vocabulary from which keywords are taken. If more than one keyword vocabulary is used, each may be presented with a prefix and a following comma, so that keywords may optionally be prefixed with the controlled vocabulary key. Example: 'GCMD:GCMD Keywords, CF:NetCDF COARDS Climate and Forecast Standard Names'.",
    )
    platform: str = Field(
        ...,
        regex=r".",
        title="Platform",
        description="Name of the platform(s) that supported the sensor data used to create this data set or product. Platforms can be of any type, including satellite, ship, station, aircraft or other. Indicate controlled vocabulary used in platform_vocabulary.",
    )
    platform_vocabulary: str = Field(
        ...,
        regex=r".",
        title="Platform Vocabulary",
        description="Controlled vocabulary for the names used in the 'platform' attribute.",
    )
    instrument: str = Field(
        ...,
        regex=r".",
        title="Instrument",
        description="Name of the contributing instrument(s) or sensor(s) used to create this data set or product. Indicate controlled vocabulary used in instrument_vocabulary.",
    )
    instrument_vocabulary: str = Field(
        ...,
        regex=r".",
        title="Instrument Vocabulary",
        description="Controlled vocabulary for the names used in the 'instrument' attribute.",
    )
    cdm_data_type: str = Field(
        ...,
        regex=r".",
        title="Common Data Model Data Type",
        description="The data type, as derived from Unidata's Common Data Model Scientific Data types and understood by THREDDS. (This is a THREDDS 'dataType', and is different from the CF NetCDF attribute 'featureType', which indicates a Discrete Sampling Geometry file in CF.).",
    )
    metadata_link: str = Field(
        ...,
        regex=r".",
        title="Metadata Link",
        description="A URL that gives the location of more complete metadata. A persistent URL is recommended for this attribute.",
    )


class IOOSGlobalAttrs(ACDDGlobalAttrs, extra=Extra.allow):
    infoUrl: str = Field(
        ...,
        regex=r".", 
        title="Info URL",
        description="URL for background information about this dataset.",
    )
    creator_country: str = Field(
        ...,
        regex=r".", 
        title="Creator Country",
        description="Country of the person or organization that operates a platform or network, which collected the observation data.",
    )
    creator_state: str = Field(
        ...,
        regex=r".", 
        title="Creator State",
        description="State or province of the person or organization that collected the data.",
    )
    creator_institution_url: str = Field(
        ...,
        regex=r".", 
        title="Creator Institution URL",
        description="URL for the institution that collected the data. For clarity, it is recommended that this field is specified even if the creator_type is institution and a creator_url is provided.",
    )
    creator_sector: str = Field(
        ...,
        regex=r".", 
        title="Creator Sector",
        description="IOOS classifier (https://mmisw.org/ont/ioos/sector) that best describes the platform (network) operator's societal sector.",
    )
    contributor_email: str = Field(
        ...,
        regex=r".", 
        title="Contributor Email(s)",
        description="IOOS classifier (https://mmisw.org/ont/ioos/sector) that best describes the platform (network) operator's societal sector.",
    )
    contributor_role_vocabulary: str = Field(
        ...,
        regex=r".", 
        title="Contributor Role Vocabulary",
        description="The URL of the controlled vocabulary used for the contributor_role attribute. The default is “https://vocab.nerc.ac.uk/collection/G04/current/”.",
    )
    contributor_url: str = Field(
        ...,
        regex=r".", 
        title="Contributor URL(s)",
        description="The URL of the individuals or institutions that contributed to the creation of this data. Multiple URLs should be given in CSV format, and presented in the same order and number as the names in contributor_names.",
    )
    publisher_country: str = Field(
        ...,
        regex=r".", 
        title="Creator Country",
        description="Country of the person or organization that distributes the data.",
    )
    publisher_state: str = Field(
        ...,
        regex=r".", 
        title="Creator State",
        description="State or province of the person or organization that distributes the data.",
    )
    platform_id: str = Field(
        ...,
        regex=r".", 
        title="Platform ID",
        description="An optional, short identifier for the platform, if the data provider prefers to define an id that differs from the dataset identifier, as specified by the id attribute. Platform_id should be a single alphanumeric string with no blank spaces.",
    )
    platform_name: str = Field(
        ...,
        regex=r".", 
        title="Platform Name",
        description="A descriptive, long name for the platform used in collecting the data. The value of platform_name will be used to label the platform in downstream applications, such as IOOS’ National Products (Environmental Sensor Map, EDS, etc).",
    )
    WMO_platform_code: str = Field(
        ...,
        regex=r".", 
        title="WMO Platform Code",
        description="The WMO identifier for the platform used to measure the data. This identifier can be any of the following types: 1. WMO ID for buoys (numeric, 5 digits), 2. WMO ID for gliders (numeric, 7 digits), 3. NWS ID (alphanumeric, 5 digits). When a dataset is assigned a wmo_platform_code it is thereby assigned a secondary Asset Identifier for the 'WMO' naming_authority. See https://ioos.github.io/ioos-metadata/ioos-metadata-profile-v1-2.html#rules-for-ioos-asset-identifier-generation for more details.",
    )
    

class ACDDDatasetConfig(DatasetConfig, extra=Extra.allow):
    attrs: ACDDGlobalAttrs = Field(
        ...,
        description="Attributes that pertain to the dataset as a whole (as opposed to"
        " attributes that are specific to individual variables.",
    )
    
    
class IOOSDatasetConfig(DatasetConfig, extra=Extra.allow):
    attrs: IOOSGlobalAttrs = Field(
        ...,
        description="Attributes that pertain to the dataset as a whole (as opposed to"
        " attributes that are specific to individual variables.",
    )


def generate_schema(dataset_config: DatasetConfig, dir: Path = Path(".vscode/schema/")):
    dir.mkdir(exist_ok=True)
    cls_mapping = {
        "retriever": RetrieverConfig,
        "dataset": dataset_config,
        "quality": QualityConfig,
        "storage": StorageConfig,
        "pipeline": PipelineConfig,
    }
    for key, config_class in cls_mapping.items():
        path = dir / f"{key}-schema.json"
        config_class.generate_schema(path)
        print(f"Wrote {key} schema file to {path}")
    print("Done!")


if __name__ == "__main__":
    generate_schema(ACDDDatasetConfig)
