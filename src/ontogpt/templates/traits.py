from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel as BaseModel, Field
import sys
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


metamodel_version = "None"
version = "None"

class ConfiguredBaseModel(BaseModel,
                validate_assignment = True,
                validate_default = True,
                extra = 'forbid',
                arbitrary_types_allowed = True,
                use_enum_values = True):
    pass


class NullDataOptions(str, Enum):
    
    
    UNSPECIFIED_METHOD_OF_ADMINISTRATION = "UNSPECIFIED_METHOD_OF_ADMINISTRATION"
    
    NOT_APPLICABLE = "NOT_APPLICABLE"
    
    NOT_MENTIONED = "NOT_MENTIONED"
    
    

class Taxon(ConfiguredBaseModel):
    
    metabolic_traits: Optional[List[str]] = Field(default_factory=list, description="""The metabolic traits for the taxon.""")
    morphological_traits: Optional[List[str]] = Field(default_factory=list, description="""The morphological traits for the taxon.""")
    genetic_traits: Optional[List[str]] = Field(default_factory=list, description="""The genetic traits for the taxon.""")
    cellular_traits: Optional[List[str]] = Field(default_factory=list, description="""The cellular traits for the taxon.""")
    ecological_traits: Optional[List[str]] = Field(default_factory=list, description="""The ecological traits for the taxon.""")
    reproductive_traits: Optional[List[str]] = Field(default_factory=list, description="""The reproductive traits for the taxon.""")
    survival_traits: Optional[List[str]] = Field(default_factory=list, description="""The survival traits for the taxon.""")
    phenotypic_plasticiticy_traits: Optional[List[str]] = Field(default_factory=list, description="""The phenotypic plasticiticy traits for the taxon.""")
    preferred_environments: Optional[List[str]] = Field(default_factory=list, description="""The preferred environments for the taxon.""")
    

class ExtractionResult(ConfiguredBaseModel):
    """
    A result of extracting knowledge on text
    """
    input_id: Optional[str] = Field(None)
    input_title: Optional[str] = Field(None)
    input_text: Optional[str] = Field(None)
    raw_completion_output: Optional[str] = Field(None)
    prompt: Optional[str] = Field(None)
    extracted_object: Optional[Any] = Field(None, description="""The complex objects extracted from the text""")
    named_entities: Optional[List[Any]] = Field(default_factory=list, description="""Named entities extracted from the text""")
    

class NamedEntity(ConfiguredBaseModel):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    

class Trait(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    

class CompoundExpression(ConfiguredBaseModel):
    
    None
    

class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    subject: Optional[str] = Field(None)
    predicate: Optional[str] = Field(None)
    object: Optional[str] = Field(None)
    qualifier: Optional[str] = Field(None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""")
    subject_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the subject of the statement, e.g. \"high dose\" or \"intravenously administered\"""")
    object_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the object of the statement, e.g. \"severe\" or \"with additional complications\"""")
    

class TextWithTriples(ConfiguredBaseModel):
    
    publication: Optional[Publication] = Field(None)
    triples: Optional[List[Triple]] = Field(default_factory=list)
    

class RelationshipType(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    

class Publication(ConfiguredBaseModel):
    
    id: Optional[str] = Field(None, description="""The publication identifier""")
    title: Optional[str] = Field(None, description="""The title of the publication""")
    abstract: Optional[str] = Field(None, description="""The abstract of the publication""")
    combined_text: Optional[str] = Field(None)
    full_text: Optional[str] = Field(None, description="""The full text of the publication""")
    

class AnnotatorResult(ConfiguredBaseModel):
    
    subject_text: Optional[str] = Field(None)
    object_id: Optional[str] = Field(None)
    object_text: Optional[str] = Field(None)
    


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Taxon.model_rebuild()
ExtractionResult.model_rebuild()
NamedEntity.model_rebuild()
Trait.model_rebuild()
CompoundExpression.model_rebuild()
Triple.model_rebuild()
TextWithTriples.model_rebuild()
RelationshipType.model_rebuild()
Publication.model_rebuild()
AnnotatorResult.model_rebuild()
    
