
# Class: Disease




URI: [ibdlit:Disease](http://w3id.org/ontogpt/ibd_literature/Disease)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[IBDAnnotations]-%20diseases%200..*>[Disease&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Disease],[IBDAnnotations])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[IBDAnnotations]-%20diseases%200..*>[Disease&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Disease],[IBDAnnotations])

## Identifier prefixes

 * MONDO

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞diseases](iBDAnnotations__diseases.md)*  <sub>0..\*</sub>  **[Disease](Disease.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
