
![MMD](pic/MDD.png)

![layers](pic/Layers.png)
A typical interaction of the application, domain and infrastructure could look like this. The user wants to book a flights route, and asks an application service in the application layer to do so. The application tier fetches the relevant domain objects from the infrastructure and invokes relevant methods on them, e.g., to check security margins to other already booked flights. Once the domain objects have made all checks and updated their status to “decided”, the application service persists the objects to the infrastructure.

## Entities
An entity is a plain object that has an identity (ID) and is potentially mutable. Each entity is uniquely identified by an ID rather than by an attribute; therefore, two entities can be considered equal (identifier equality) if both of them have the same ID even though they have different attributes

## Value Objects
In DDD, value objects differ from entities by lacking the concept of identity. We do not care who they are but rather what they are. They are defined by their attributes and shohuld be immutable. Being immutable, and having no identity, Value Objects can be shared.

## Service
A service is not about the object performing the service, but is related to the objects the operations are performed on/for. An object does not have an internal state, and its purpose is to simply provide functionality for the domain.
There are three characteristics of a Service:
1. The operation performed by the Service refers to a domain concept which does not naturally belong to an Entity or Value Object.
2. The operation performed refers to other objects in the domain.
3. The operation is stateless.

If the operation performed conceptually belongs to the application layer, then the Service should be placed there. If the operation is about domain objects, and is strictly related to the domain, serving a domain need, then it should belong to the domain layer.

## Modules
high level of cohesion and a low level of coupling(高内聚低耦合)<br>
Modules should be made up of elements which functionally or logically belong together assuring cohesion. Modules should have well defined interfaces which are accessed by other modules. Instead of calling three objects of a module, it is better to access one interface, because it reduces coupling.

## Aggregate
An Aggregate is a group of associated objects which are considered as one unit with regard to data changes. Each Aggregate has one root. The root is an Entity, and it is the only object accessible from outside. The root can hold references to any of the aggregate objects, and the other objects can hold references to each other, but an outside object can hold references only to the root object. Choose one Entity to be the root of each Aggregate, and control all access to the objects inside the boundary through the root.

## Factory
Entities and Aggregates can often be large and complex – too complex to create in the constructor of the root entity. There are times when a Factory is not needed, and a simple constructor is enough. Use a constructor when:
* The construction is not complicated.
* The creation of an object does not involve the creation of others, and all the attributes needed are passed via the constructor.
* The client is interested in the implementation, perhaps wants to choose the Strategy used.
* The class is the type. There is no hierarchy involved, so no need to choose between a list of concrete implementations.

## Repositories
In a nutshell, it is API between client and storage. A Repository may contain detailed information used to access the infrastructure, but its interface should be simple. A Repository should have a set of methods used to retrieve objects.