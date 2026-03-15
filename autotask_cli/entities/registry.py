from .base import BaseEntity

# =============================================================================
# CATEGORY 1: Companies & CRM
# =============================================================================

class Companies(BaseEntity):
    endpoint = "Companies"
    display_fields = ["id", "companyName", "isActive"]
    required_fields = ["companyName", "companyType", "phone", "ownerResourceID"]

class CompanyAlerts(BaseEntity):
    endpoint = "CompanyAlerts"
    display_fields = ["id", "companyID", "alertTypeID"]
    required_fields = ["companyID", "alertTypeID", "alertText"]

class CompanyAttachments(BaseEntity):
    endpoint = "CompanyAttachments"
    display_fields = ["id", "companyID", "title"]
    required_fields = ["companyID"]
    parent_endpoint = "Companies"
    parent_id_field = "companyID"

class CompanyCategories(BaseEntity):
    endpoint = "CompanyCategories"
    display_fields = ["id", "name", "isActive"]
    required_fields = ["name"]
    can_delete = False

class CompanyLocations(BaseEntity):
    endpoint = "CompanyLocations"
    display_fields = ["id", "companyID", "name", "isActive"]
    required_fields = ["companyID", "name"]

class CompanyNotes(BaseEntity):
    endpoint = "CompanyNotes"
    display_fields = ["id", "companyID", "title", "lastModifiedDate"]
    required_fields = ["companyID", "title"]
    parent_endpoint = "Companies"
    parent_id_field = "companyID"

class CompanyNoteAttachments(BaseEntity):
    endpoint = "CompanyNoteAttachments"
    display_fields = ["id", "parentID", "title"]
    required_fields = ["parentID"]

class CompanySiteConfigurations(BaseEntity):
    endpoint = "CompanySiteConfigurations"
    display_fields = ["id", "companyID"]
    required_fields = ["companyID"]

class CompanyTeams(BaseEntity):
    endpoint = "CompanyTeams"
    display_fields = ["id", "companyID", "resourceID"]
    required_fields = ["companyID", "resourceID"]

class CompanyToDos(BaseEntity):
    endpoint = "CompanyToDos"
    display_fields = ["id", "companyID", "actionType", "assignedToResourceID"]
    required_fields = ["companyID", "actionType", "assignedToResourceID", "startDateTime", "endDateTime"]


# =============================================================================
# CATEGORY 2: Contacts
# =============================================================================

class Contacts(BaseEntity):
    endpoint = "Contacts"
    display_fields = ["id", "firstName", "lastName", "companyID"]
    required_fields = ["firstName", "lastName", "companyID", "isActive"]
    parent_endpoint = "Companies"
    parent_id_field = "companyID"

class ContactBillingProductAssociations(BaseEntity):
    endpoint = "ContactBillingProductAssociations"
    display_fields = ["id", "contactID", "billingProductID"]
    required_fields = ["contactID", "billingProductID"]

class ContactGroupContacts(BaseEntity):
    endpoint = "ContactGroupContacts"
    display_fields = ["id", "contactGroupID", "contactID"]
    required_fields = ["contactGroupID", "contactID"]

class ContactGroups(BaseEntity):
    endpoint = "ContactGroups"
    display_fields = ["id", "name", "isActive"]
    required_fields = ["name"]


# =============================================================================
# CATEGORY 3: Tickets & Service Desk
# =============================================================================

class Tickets(BaseEntity):
    endpoint = "Tickets"
    display_fields = ["id", "ticketNumber", "title", "status"]
    required_fields = ["title", "companyID", "status", "priority", "queueID"]

class TicketAdditionalConfigurationItems(BaseEntity):
    endpoint = "TicketAdditionalConfigurationItems"
    display_fields = ["id", "ticketID", "configurationItemID"]
    required_fields = ["ticketID", "configurationItemID"]

class TicketAdditionalContacts(BaseEntity):
    endpoint = "TicketAdditionalContacts"
    display_fields = ["id", "ticketID", "contactID"]
    required_fields = ["ticketID", "contactID"]

class TicketAttachments(BaseEntity):
    endpoint = "TicketAttachments"
    display_fields = ["id", "ticketID", "title"]
    required_fields = ["ticketID"]
    parent_endpoint = "Tickets"
    parent_id_field = "ticketID"

class TicketCategories(BaseEntity):
    endpoint = "TicketCategories"
    display_fields = ["id", "name", "isActive"]
    required_fields = ["name"]
    can_delete = False

class TicketCategoryFieldDefaults(BaseEntity):
    endpoint = "TicketCategoryFieldDefaults"
    display_fields = ["id", "ticketCategoryID"]
    required_fields = ["ticketCategoryID"]

class TicketChangeRequestApprovals(BaseEntity):
    endpoint = "TicketChangeRequestApprovals"
    display_fields = ["id", "ticketID", "resourceID"]
    required_fields = ["ticketID"]

class TicketCharges(BaseEntity):
    endpoint = "TicketCharges"
    display_fields = ["id", "ticketID", "name", "datePurchased"]
    required_fields = ["ticketID", "name"]

class TicketChecklistItems(BaseEntity):
    endpoint = "TicketChecklistItems"
    display_fields = ["id", "ticketID", "itemName"]
    required_fields = ["ticketID", "itemName"]

class TicketChecklistLibraries(BaseEntity):
    endpoint = "TicketChecklistLibraries"
    display_fields = ["id", "ticketID", "checklistLibraryID"]
    required_fields = ["ticketID", "checklistLibraryID"]

class TicketHistory(BaseEntity):
    endpoint = "TicketHistory"
    display_fields = ["id", "ticketID", "fieldName", "date"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class TicketNotes(BaseEntity):
    endpoint = "TicketNotes"
    display_fields = ["id", "ticketID", "title", "noteType"]
    required_fields = ["ticketID", "title"]
    parent_endpoint = "Tickets"
    parent_id_field = "ticketID"

class TicketNoteAttachments(BaseEntity):
    endpoint = "TicketNoteAttachments"
    display_fields = ["id", "parentID", "title"]
    required_fields = ["parentID"]

class TicketRmaCredits(BaseEntity):
    endpoint = "TicketRmaCredits"
    display_fields = ["id", "ticketID", "creditAmount"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class TicketSecondaryResources(BaseEntity):
    endpoint = "TicketSecondaryResources"
    display_fields = ["id", "ticketID", "resourceID"]
    required_fields = ["ticketID", "resourceID"]

class TicketTagAssociations(BaseEntity):
    endpoint = "TicketTagAssociations"
    display_fields = ["id", "ticketID", "tagID"]
    required_fields = ["ticketID", "tagID"]


# =============================================================================
# CATEGORY 4: Projects & Tasks
# =============================================================================

class Projects(BaseEntity):
    endpoint = "Projects"
    display_fields = ["id", "projectName", "companyID", "status"]
    required_fields = ["projectName", "companyID", "type", "startDateTime", "endDateTime"]

class ProjectAttachments(BaseEntity):
    endpoint = "ProjectAttachments"
    display_fields = ["id", "projectID", "title"]
    required_fields = ["projectID"]
    parent_endpoint = "Projects"
    parent_id_field = "projectID"

class ProjectCharges(BaseEntity):
    endpoint = "ProjectCharges"
    display_fields = ["id", "projectID", "name", "datePurchased"]
    required_fields = ["projectID", "name"]

class ProjectNotes(BaseEntity):
    endpoint = "ProjectNotes"
    display_fields = ["id", "projectID", "title", "noteType"]
    required_fields = ["projectID", "title"]
    parent_endpoint = "Projects"
    parent_id_field = "projectID"

class ProjectNoteAttachments(BaseEntity):
    endpoint = "ProjectNoteAttachments"
    display_fields = ["id", "parentID", "title"]
    required_fields = ["parentID"]

class Phases(BaseEntity):
    endpoint = "Phases"
    display_fields = ["id", "projectID", "title"]
    required_fields = ["projectID", "title"]

class Tasks(BaseEntity):
    endpoint = "Tasks"
    display_fields = ["id", "projectID", "title", "status"]
    required_fields = ["projectID", "title", "phaseID", "status"]

class TaskAttachments(BaseEntity):
    endpoint = "TaskAttachments"
    display_fields = ["id", "taskID", "title"]
    required_fields = ["taskID"]
    parent_endpoint = "Tasks"
    parent_id_field = "taskID"

class TaskNotes(BaseEntity):
    endpoint = "TaskNotes"
    display_fields = ["id", "taskID", "title", "noteType"]
    required_fields = ["taskID", "title"]
    parent_endpoint = "Tasks"
    parent_id_field = "taskID"

class TaskNoteAttachments(BaseEntity):
    endpoint = "TaskNoteAttachments"
    display_fields = ["id", "parentID", "title"]
    required_fields = ["parentID"]

class TaskPredecessors(BaseEntity):
    endpoint = "TaskPredecessors"
    display_fields = ["id", "predecessorTaskID", "successorTaskID"]
    required_fields = ["predecessorTaskID", "successorTaskID"]

class TaskSecondaryResources(BaseEntity):
    endpoint = "TaskSecondaryResources"
    display_fields = ["id", "taskID", "resourceID"]
    required_fields = ["taskID", "resourceID"]


# =============================================================================
# CATEGORY 5: Contracts
# =============================================================================

class Contracts(BaseEntity):
    endpoint = "Contracts"
    display_fields = ["id", "contractName", "companyID", "contractType", "status"]
    required_fields = ["contractName", "companyID", "contractType", "startDate", "endDate", "timeReportingRequiresStartAndStopTimes"]

class ContractBillingRules(BaseEntity):
    endpoint = "ContractBillingRules"
    display_fields = ["id", "contractID"]
    required_fields = ["contractID"]

class ContractBlockHourFactors(BaseEntity):
    endpoint = "ContractBlockHourFactors"
    display_fields = ["id", "contractID", "roleID"]
    required_fields = ["contractID", "roleID"]

class ContractBlocks(BaseEntity):
    endpoint = "ContractBlocks"
    display_fields = ["id", "contractID", "hours", "startDate"]
    required_fields = ["contractID", "hours", "startDate"]

class ContractCharges(BaseEntity):
    endpoint = "ContractCharges"
    display_fields = ["id", "contractID", "name", "datePurchased"]
    required_fields = ["contractID", "name"]

class ContractExclusionBillingCodes(BaseEntity):
    endpoint = "ContractExclusionBillingCodes"
    display_fields = ["id", "contractID", "billingCodeID"]
    required_fields = ["contractID", "billingCodeID"]

class ContractExclusionRoles(BaseEntity):
    endpoint = "ContractExclusionRoles"
    display_fields = ["id", "contractID", "roleID"]
    required_fields = ["contractID", "roleID"]

class ContractExclusionSets(BaseEntity):
    endpoint = "ContractExclusionSets"
    display_fields = ["id", "name", "isActive"]
    required_fields = ["name"]

class ContractExclusionSetExcludedRoles(BaseEntity):
    endpoint = "ContractExclusionSetExcludedRoles"
    display_fields = ["id", "contractExclusionSetID", "roleID"]
    required_fields = ["contractExclusionSetID", "roleID"]

class ContractExclusionSetExcludedWorkTypes(BaseEntity):
    endpoint = "ContractExclusionSetExcludedWorkTypes"
    display_fields = ["id", "contractExclusionSetID", "workTypeID"]
    required_fields = ["contractExclusionSetID", "workTypeID"]

class ContractMilestones(BaseEntity):
    endpoint = "ContractMilestones"
    display_fields = ["id", "contractID", "title", "status"]
    required_fields = ["contractID", "title"]

class ContractNotes(BaseEntity):
    endpoint = "ContractNotes"
    display_fields = ["id", "contractID", "title"]
    required_fields = ["contractID", "title"]
    parent_endpoint = "Contracts"
    parent_id_field = "contractID"

class ContractNoteAttachments(BaseEntity):
    endpoint = "ContractNoteAttachments"
    display_fields = ["id", "parentID", "title"]
    required_fields = ["parentID"]

class ContractRates(BaseEntity):
    endpoint = "ContractRates"
    display_fields = ["id", "contractID", "roleID"]
    required_fields = ["contractID"]

class ContractRetainers(BaseEntity):
    endpoint = "ContractRetainers"
    display_fields = ["id", "contractID", "amount", "startDate"]
    required_fields = ["contractID", "amount", "startDate"]

class ContractRoleCosts(BaseEntity):
    endpoint = "ContractRoleCosts"
    display_fields = ["id", "contractID", "roleID"]
    required_fields = ["contractID", "roleID"]

class ContractServices(BaseEntity):
    endpoint = "ContractServices"
    display_fields = ["id", "contractID", "serviceID"]
    required_fields = ["contractID", "serviceID"]

class ContractServiceAdjustments(BaseEntity):
    endpoint = "ContractServiceAdjustments"
    display_fields = ["id", "contractServiceID", "adjustedUnitCount"]
    required_fields = ["contractServiceID"]

class ContractServiceBundles(BaseEntity):
    endpoint = "ContractServiceBundles"
    display_fields = ["id", "contractID", "serviceBundleID"]
    required_fields = ["contractID", "serviceBundleID"]

class ContractServiceBundleAdjustments(BaseEntity):
    endpoint = "ContractServiceBundleAdjustments"
    display_fields = ["id", "contractServiceBundleID", "adjustedUnitCount"]
    required_fields = ["contractServiceBundleID"]

class ContractServiceBundleUnits(BaseEntity):
    endpoint = "ContractServiceBundleUnits"
    display_fields = ["id", "contractServiceBundleID", "units"]
    required_fields = ["contractServiceBundleID"]

class ContractServiceUnits(BaseEntity):
    endpoint = "ContractServiceUnits"
    display_fields = ["id", "contractServiceID", "units"]
    required_fields = ["contractServiceID"]

class ContractTicketPurchases(BaseEntity):
    endpoint = "ContractTicketPurchases"
    display_fields = ["id", "contractID", "ticketsPurchased"]
    required_fields = ["contractID", "ticketsPurchased"]


# =============================================================================
# CATEGORY 6: Configuration Items (Assets)
# =============================================================================

class ConfigurationItems(BaseEntity):
    endpoint = "ConfigurationItems"
    display_fields = ["id", "companyID", "referenceTitle", "isActive"]
    required_fields = ["companyID", "configurationItemType"]

class ConfigurationItemAttachments(BaseEntity):
    endpoint = "ConfigurationItemAttachments"
    display_fields = ["id", "configurationItemID", "title"]
    required_fields = ["configurationItemID"]
    parent_endpoint = "ConfigurationItems"
    parent_id_field = "configurationItemID"

class ConfigurationItemBillingProductAssociations(BaseEntity):
    endpoint = "ConfigurationItemBillingProductAssociations"
    display_fields = ["id", "configurationItemID", "billingProductID"]
    required_fields = ["configurationItemID", "billingProductID"]

class ConfigurationItemCategories(BaseEntity):
    endpoint = "ConfigurationItemCategories"
    display_fields = ["id", "name", "isActive"]
    required_fields = ["name"]

class ConfigurationItemCategoryUdfAssociations(BaseEntity):
    endpoint = "ConfigurationItemCategoryUdfAssociations"
    display_fields = ["id", "configurationItemCategoryID", "userDefinedFieldDefinitionID"]
    required_fields = ["configurationItemCategoryID", "userDefinedFieldDefinitionID"]

class ConfigurationItemDnsRecords(BaseEntity):
    endpoint = "ConfigurationItemDnsRecords"
    display_fields = ["id", "configurationItemID", "dnsType", "hostName"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class ConfigurationItemNotes(BaseEntity):
    endpoint = "ConfigurationItemNotes"
    display_fields = ["id", "configurationItemID", "title"]
    required_fields = ["configurationItemID", "title"]
    parent_endpoint = "ConfigurationItems"
    parent_id_field = "configurationItemID"

class ConfigurationItemNoteAttachments(BaseEntity):
    endpoint = "ConfigurationItemNoteAttachments"
    display_fields = ["id", "parentID", "title"]
    required_fields = ["parentID"]

class ConfigurationItemRelatedItems(BaseEntity):
    endpoint = "ConfigurationItemRelatedItems"
    display_fields = ["id", "configurationItemID", "relatedConfigurationItemID"]
    required_fields = ["configurationItemID", "relatedConfigurationItemID"]

class ConfigurationItemSslSubjectAlternativeName(BaseEntity):
    endpoint = "ConfigurationItemSslSubjectAlternativeName"
    display_fields = ["id", "configurationItemID", "subjectAlternativeName"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class ConfigurationItemTypes(BaseEntity):
    endpoint = "ConfigurationItemTypes"
    display_fields = ["id", "name", "isActive"]
    required_fields = ["name"]
    can_delete = False


# =============================================================================
# CATEGORY 7: Billing & Finance
# =============================================================================

class BillingCodes(BaseEntity):
    endpoint = "BillingCodes"
    display_fields = ["id", "name", "billingCodeType", "isActive"]
    required_fields = ["name", "billingCodeType"]

class BillingItems(BaseEntity):
    endpoint = "BillingItems"
    display_fields = ["id", "type", "description", "totalAmount"]
    required_fields = []
    can_create = False
    can_delete = False

class BillingItemApprovalLevels(BaseEntity):
    endpoint = "BillingItemApprovalLevels"
    display_fields = ["id", "timeEntryID", "approvalLevel"]
    required_fields = ["timeEntryID", "approvalLevel"]

class Invoices(BaseEntity):
    endpoint = "Invoices"
    display_fields = ["id", "companyID", "invoiceNumber", "invoiceTotal"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class InvoiceTemplates(BaseEntity):
    endpoint = "InvoiceTemplates"
    display_fields = ["id", "name"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class AdditionalInvoiceFieldValues(BaseEntity):
    endpoint = "AdditionalInvoiceFieldValues"
    display_fields = ["id", "invoiceID", "additionalInvoiceFieldID"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False


# =============================================================================
# CATEGORY 8: Opportunities & Sales
# =============================================================================

class Opportunities(BaseEntity):
    endpoint = "Opportunities"
    display_fields = ["id", "title", "companyID", "status"]
    required_fields = ["title", "companyID", "status", "ownerResourceID"]

class OpportunityAttachments(BaseEntity):
    endpoint = "OpportunityAttachments"
    display_fields = ["id", "opportunityID", "title"]
    required_fields = ["opportunityID"]
    parent_endpoint = "Opportunities"
    parent_id_field = "opportunityID"

class OpportunityCategories(BaseEntity):
    endpoint = "OpportunityCategories"
    display_fields = ["id", "name"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class SalesOrders(BaseEntity):
    endpoint = "SalesOrders"
    display_fields = ["id", "opportunityID", "status"]
    required_fields = ["opportunityID", "status"]

class SalesOrderAttachments(BaseEntity):
    endpoint = "SalesOrderAttachments"
    display_fields = ["id", "parentID", "title"]
    required_fields = ["parentID"]

class Quotes(BaseEntity):
    endpoint = "Quotes"
    display_fields = ["id", "name", "opportunityID", "billToCompanyID"]
    required_fields = ["name", "opportunityID"]

class QuoteItems(BaseEntity):
    endpoint = "QuoteItems"
    display_fields = ["id", "quoteID", "name", "quantity", "unitPrice"]
    required_fields = ["quoteID", "type"]

class QuoteLocations(BaseEntity):
    endpoint = "QuoteLocations"
    display_fields = ["id", "address1", "city", "state"]
    required_fields = []

class QuoteTemplates(BaseEntity):
    endpoint = "QuoteTemplates"
    display_fields = ["id", "name"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False


# =============================================================================
# CATEGORY 9: Resources & HR
# =============================================================================

class Resources(BaseEntity):
    endpoint = "Resources"
    display_fields = ["id", "firstName", "lastName", "email", "isActive"]
    required_fields = ["firstName", "lastName", "email", "resourceType"]

class ResourceAttachments(BaseEntity):
    endpoint = "ResourceAttachments"
    display_fields = ["id", "resourceID", "title"]
    required_fields = ["resourceID"]
    parent_endpoint = "Resources"
    parent_id_field = "resourceID"

class ResourceDailyAvailabilities(BaseEntity):
    endpoint = "ResourceDailyAvailabilities"
    display_fields = ["id", "resourceID", "availableHours"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class ResourceRoles(BaseEntity):
    endpoint = "ResourceRoles"
    display_fields = ["id", "resourceID", "roleID"]
    required_fields = ["resourceID", "roleID"]

class ResourceRoleDepartments(BaseEntity):
    endpoint = "ResourceRoleDepartments"
    display_fields = ["id", "resourceID", "roleID", "departmentID"]
    required_fields = ["resourceID", "roleID", "departmentID"]

class ResourceRoleQueues(BaseEntity):
    endpoint = "ResourceRoleQueues"
    display_fields = ["id", "resourceID", "roleID", "queueID"]
    required_fields = ["resourceID", "roleID", "queueID"]

class ResourceServiceDeskRoles(BaseEntity):
    endpoint = "ResourceServiceDeskRoles"
    display_fields = ["id", "resourceID", "roleID"]
    required_fields = ["resourceID", "roleID"]

class ResourceSkills(BaseEntity):
    endpoint = "ResourceSkills"
    display_fields = ["id", "resourceID", "skillID", "skillLevel"]
    required_fields = ["resourceID", "skillID"]

class ResourceTimeOffBalances(BaseEntity):
    endpoint = "ResourceTimeOffBalances"
    display_fields = ["id", "resourceID", "balance"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class ResourceTimeOffAdditional(BaseEntity):
    endpoint = "ResourceTimeOffAdditional"
    display_fields = ["id", "resourceID", "hours"]
    required_fields = ["resourceID"]
    can_delete = False

class ResourceTimeOffApprovers(BaseEntity):
    endpoint = "ResourceTimeOffApprovers"
    display_fields = ["id", "resourceID", "approverResourceID"]
    required_fields = ["resourceID"]
    can_delete = False

class Roles(BaseEntity):
    endpoint = "Roles"
    display_fields = ["id", "name", "isActive"]
    required_fields = ["name"]


# =============================================================================
# CATEGORY 10: Time & Expenses
# =============================================================================

class TimeEntries(BaseEntity):
    endpoint = "TimeEntries"
    display_fields = ["id", "resourceID", "ticketID", "dateWorked", "hoursWorked"]
    required_fields = ["resourceID", "dateWorked"]

class TimeEntryAttachments(BaseEntity):
    endpoint = "TimeEntryAttachments"
    display_fields = ["id", "timeEntryID", "title"]
    required_fields = ["timeEntryID"]
    parent_endpoint = "TimeEntries"
    parent_id_field = "timeEntryID"

class ExpenseItems(BaseEntity):
    endpoint = "ExpenseItems"
    display_fields = ["id", "expenseReportID", "description", "expenseAmount"]
    required_fields = ["expenseReportID", "description"]

class ExpenseItemAttachments(BaseEntity):
    endpoint = "ExpenseItemAttachments"
    display_fields = ["id", "parentID", "title"]
    required_fields = ["parentID"]

class ExpenseReports(BaseEntity):
    endpoint = "ExpenseReports"
    display_fields = ["id", "name", "resourceID", "status"]
    required_fields = ["name", "resourceID"]

class ExpenseReportAttachments(BaseEntity):
    endpoint = "ExpenseReportAttachments"
    display_fields = ["id", "parentID", "title"]
    required_fields = ["parentID"]

class TimeOffRequests(BaseEntity):
    endpoint = "TimeOffRequests"
    display_fields = ["id", "resourceID", "startDate", "endDate", "status"]
    required_fields = ["resourceID", "startDate", "endDate"]

class TimeOffRequestsApprove(BaseEntity):
    endpoint = "TimeOffRequestsApprove"
    display_fields = ["id"]
    required_fields = ["timeOffRequestID"]
    can_update = False
    can_delete = False

class TimeOffRequestsReject(BaseEntity):
    endpoint = "TimeOffRequestsReject"
    display_fields = ["id"]
    required_fields = ["timeOffRequestID"]
    can_update = False
    can_delete = False


# =============================================================================
# CATEGORY 11: Products & Inventory
# =============================================================================

class Products(BaseEntity):
    endpoint = "Products"
    display_fields = ["id", "name", "isActive", "unitPrice"]
    required_fields = ["name"]

class ProductNotes(BaseEntity):
    endpoint = "ProductNotes"
    display_fields = ["id", "productID", "title"]
    required_fields = ["productID", "title"]
    parent_endpoint = "Products"
    parent_id_field = "productID"

class ProductTiers(BaseEntity):
    endpoint = "ProductTiers"
    display_fields = ["id", "productID", "unitPrice"]
    required_fields = ["productID"]

class ProductVendors(BaseEntity):
    endpoint = "ProductVendors"
    display_fields = ["id", "productID", "vendorID"]
    required_fields = ["productID", "vendorID"]

class InventoryItems(BaseEntity):
    endpoint = "InventoryItems"
    display_fields = ["id", "productID", "inventoryLocationID"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class InventoryItemSerialNumbers(BaseEntity):
    endpoint = "InventoryItemSerialNumbers"
    display_fields = ["id", "inventoryItemID", "serialNumber"]
    required_fields = ["inventoryItemID", "serialNumber"]

class InventoryLocations(BaseEntity):
    endpoint = "InventoryLocations"
    display_fields = ["id", "name", "isActive"]
    required_fields = ["name"]

class InventoryProducts(BaseEntity):
    endpoint = "InventoryProducts"
    display_fields = ["id", "productID", "inventoryLocationID", "quantityOnHand"]
    required_fields = ["productID", "inventoryLocationID"]

class InventoryStockedItems(BaseEntity):
    endpoint = "InventoryStockedItems"
    display_fields = ["id", "inventoryProductID", "serialNumber"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class InventoryStockedItemsAdd(BaseEntity):
    endpoint = "InventoryStockedItemsAdd"
    display_fields = ["id"]
    required_fields = ["inventoryProductID", "quantityToAdd"]
    can_update = False
    can_delete = False

class InventoryStockedItemsRemove(BaseEntity):
    endpoint = "InventoryStockedItemsRemove"
    display_fields = ["id"]
    required_fields = ["inventoryProductID", "quantityToRemove"]
    can_update = False
    can_delete = False

class InventoryStockedItemsTransfer(BaseEntity):
    endpoint = "InventoryStockedItemsTransfer"
    display_fields = ["id"]
    required_fields = ["inventoryProductID", "transferToInventoryLocationID", "quantityToTransfer"]
    can_update = False
    can_delete = False

class InventoryTransfers(BaseEntity):
    endpoint = "InventoryTransfers"
    display_fields = ["id", "productID", "fromInventoryLocationID", "toInventoryLocationID"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False


# =============================================================================
# CATEGORY 12: Knowledgebase & Articles
# =============================================================================

class KnowledgeBaseArticles(BaseEntity):
    endpoint = "KnowledgeBaseArticles"
    display_fields = ["id", "title", "isPublished"]
    required_fields = ["title"]

class KnowledgeBaseCategories(BaseEntity):
    endpoint = "KnowledgeBaseCategories"
    display_fields = ["id", "name"]
    required_fields = ["name"]

class ArticleAttachments(BaseEntity):
    endpoint = "ArticleAttachments"
    display_fields = ["id", "articleID", "title"]
    required_fields = ["articleID"]

class ArticleConfigurationItemCategoryAssociations(BaseEntity):
    endpoint = "ArticleConfigurationItemCategoryAssociations"
    display_fields = ["id", "articleID", "configurationItemCategoryID"]
    required_fields = ["articleID", "configurationItemCategoryID"]

class ArticleNotes(BaseEntity):
    endpoint = "ArticleNotes"
    display_fields = ["id", "knowledgeBaseArticleID", "title"]
    required_fields = ["knowledgeBaseArticleID", "title"]

class ArticlePlainTextContent(BaseEntity):
    endpoint = "ArticlePlainTextContent"
    display_fields = ["id", "knowledgeBaseArticleID"]
    required_fields = ["knowledgeBaseArticleID"]

class ArticleTagAssociations(BaseEntity):
    endpoint = "ArticleTagAssociations"
    display_fields = ["id", "articleID", "tagID"]
    required_fields = ["articleID", "tagID"]

class ArticleTicketAssociations(BaseEntity):
    endpoint = "ArticleTicketAssociations"
    display_fields = ["id", "articleID", "ticketID"]
    required_fields = ["articleID", "ticketID"]

class ArticleToArticleAssociations(BaseEntity):
    endpoint = "ArticleToArticleAssociations"
    display_fields = ["id", "articleID", "relatedArticleID"]
    required_fields = ["articleID", "relatedArticleID"]

class ArticleToDocumentAssociations(BaseEntity):
    endpoint = "ArticleToDocumentAssociations"
    display_fields = ["id", "articleID", "documentID"]
    required_fields = ["articleID", "documentID"]


# =============================================================================
# CATEGORY 13: Documents
# =============================================================================

class Documents(BaseEntity):
    endpoint = "Documents"
    display_fields = ["id", "title", "documentType", "isPublished"]
    required_fields = ["title"]

class DocumentAttachments(BaseEntity):
    endpoint = "DocumentAttachments"
    display_fields = ["id", "documentID", "title"]
    required_fields = ["documentID"]

class DocumentCategories(BaseEntity):
    endpoint = "DocumentCategories"
    display_fields = ["id", "name"]
    required_fields = ["name"]

class DocumentChecklistItems(BaseEntity):
    endpoint = "DocumentChecklistItems"
    display_fields = ["id", "documentID", "itemName"]
    required_fields = ["documentID", "itemName"]

class DocumentChecklistLibraries(BaseEntity):
    endpoint = "DocumentChecklistLibraries"
    display_fields = ["id", "documentID", "checklistLibraryID"]
    required_fields = ["documentID", "checklistLibraryID"]

class DocumentConfigurationItemAssociations(BaseEntity):
    endpoint = "DocumentConfigurationItemAssociations"
    display_fields = ["id", "documentID", "configurationItemID"]
    required_fields = ["documentID", "configurationItemID"]

class DocumentConfigurationItemCategoryAssociations(BaseEntity):
    endpoint = "DocumentConfigurationItemCategoryAssociations"
    display_fields = ["id", "documentID", "configurationItemCategoryID"]
    required_fields = ["documentID", "configurationItemCategoryID"]

class DocumentNotes(BaseEntity):
    endpoint = "DocumentNotes"
    display_fields = ["id", "documentID", "title"]
    required_fields = ["documentID", "title"]

class DocumentTagAssociations(BaseEntity):
    endpoint = "DocumentTagAssociations"
    display_fields = ["id", "documentID", "tagID"]
    required_fields = ["documentID", "tagID"]

class DocumentTicketAssociations(BaseEntity):
    endpoint = "DocumentTicketAssociations"
    display_fields = ["id", "documentID", "ticketID"]
    required_fields = ["documentID", "ticketID"]

class DocumentToArticleAssociations(BaseEntity):
    endpoint = "DocumentToArticleAssociations"
    display_fields = ["id", "documentID", "articleID"]
    required_fields = ["documentID", "articleID"]


# =============================================================================
# CATEGORY 14: Service Calls
# =============================================================================

class ServiceCalls(BaseEntity):
    endpoint = "ServiceCalls"
    display_fields = ["id", "companyID", "description", "status"]
    required_fields = ["companyID", "startDateTime", "endDateTime"]

class ServiceCallTasks(BaseEntity):
    endpoint = "ServiceCallTasks"
    display_fields = ["id", "serviceCallID", "taskID"]
    required_fields = ["serviceCallID", "taskID"]

class ServiceCallTaskResources(BaseEntity):
    endpoint = "ServiceCallTaskResources"
    display_fields = ["id", "serviceCallTaskID", "resourceID"]
    required_fields = ["serviceCallTaskID", "resourceID"]

class ServiceCallTickets(BaseEntity):
    endpoint = "ServiceCallTickets"
    display_fields = ["id", "serviceCallID", "ticketID"]
    required_fields = ["serviceCallID", "ticketID"]

class ServiceCallTicketResources(BaseEntity):
    endpoint = "ServiceCallTicketResources"
    display_fields = ["id", "serviceCallTicketID", "resourceID"]
    required_fields = ["serviceCallTicketID", "resourceID"]


# =============================================================================
# CATEGORY 15: Services & Subscriptions
# =============================================================================

class Services(BaseEntity):
    endpoint = "Services"
    display_fields = ["id", "name", "isActive", "unitPrice"]
    required_fields = ["name"]

class ServiceBundles(BaseEntity):
    endpoint = "ServiceBundles"
    display_fields = ["id", "serviceBundleName", "isActive"]
    required_fields = ["serviceBundleName"]

class ServiceBundleServices(BaseEntity):
    endpoint = "ServiceBundleServices"
    display_fields = ["id", "serviceBundleID", "serviceID"]
    required_fields = ["serviceBundleID", "serviceID"]

class Subscriptions(BaseEntity):
    endpoint = "Subscriptions"
    display_fields = ["id", "materialCodeID", "description", "status"]
    required_fields = ["materialCodeID"]

class SubscriptionPeriods(BaseEntity):
    endpoint = "SubscriptionPeriods"
    display_fields = ["id", "subscriptionID", "periodDate"]
    required_fields = ["subscriptionID"]

class ServiceLevelAgreementResults(BaseEntity):
    endpoint = "ServiceLevelAgreementResults"
    display_fields = ["id", "ticketID", "serviceLevelAgreementName"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False


# =============================================================================
# CATEGORY 16: Purchase Orders
# =============================================================================

class PurchaseOrders(BaseEntity):
    endpoint = "PurchaseOrders"
    display_fields = ["id", "vendorID", "status", "shippingType"]
    required_fields = ["vendorID"]

class PurchaseOrderItems(BaseEntity):
    endpoint = "PurchaseOrderItems"
    display_fields = ["id", "purchaseOrderID", "productID", "quantity", "unitCost"]
    required_fields = ["purchaseOrderID"]

class PurchaseOrderItemReceiving(BaseEntity):
    endpoint = "PurchaseOrderItemReceiving"
    display_fields = ["id", "purchaseOrderItemID", "quantityReceived"]
    required_fields = ["purchaseOrderItemID"]

class PurchaseApprovals(BaseEntity):
    endpoint = "PurchaseApprovals"
    display_fields = ["id", "purchaseOrderID", "isApproved"]
    required_fields = ["purchaseOrderID"]


# =============================================================================
# CATEGORY 17: Pricing
# =============================================================================

class PriceListMaterialCodes(BaseEntity):
    endpoint = "PriceListMaterialCodes"
    display_fields = ["id", "materialCodeID", "currencyID"]
    required_fields = []
    can_create = False
    can_delete = False

class PriceListProducts(BaseEntity):
    endpoint = "PriceListProducts"
    display_fields = ["id", "productID", "currencyID", "unitPrice"]
    required_fields = []
    can_create = False
    can_delete = False

class PriceListProductTiers(BaseEntity):
    endpoint = "PriceListProductTiers"
    display_fields = ["id", "productID", "currencyID"]
    required_fields = []
    can_create = False
    can_delete = False

class PriceListRoles(BaseEntity):
    endpoint = "PriceListRoles"
    display_fields = ["id", "roleID", "currencyID"]
    required_fields = []
    can_create = False
    can_delete = False

class PriceListServices(BaseEntity):
    endpoint = "PriceListServices"
    display_fields = ["id", "serviceID", "currencyID", "unitPrice"]
    required_fields = []
    can_create = False
    can_delete = False

class PriceListServiceBundles(BaseEntity):
    endpoint = "PriceListServiceBundles"
    display_fields = ["id", "serviceBundleID", "currencyID"]
    required_fields = []
    can_create = False
    can_delete = False

class PriceListWorkTypeModifiers(BaseEntity):
    endpoint = "PriceListWorkTypeModifiers"
    display_fields = ["id", "workTypeModifierID", "currencyID"]
    required_fields = []
    can_create = False
    can_delete = False


# =============================================================================
# CATEGORY 18: Admin & System
# =============================================================================

class ActionTypes(BaseEntity):
    endpoint = "ActionTypes"
    display_fields = ["id", "name", "isActive"]
    required_fields = ["name"]

class Appointments(BaseEntity):
    endpoint = "Appointments"
    display_fields = ["id", "title", "startDateTime", "endDateTime"]
    required_fields = ["title", "startDateTime", "endDateTime"]

class AttachmentInfo(BaseEntity):
    endpoint = "AttachmentInfo"
    display_fields = ["id", "parentType", "parentID", "title"]
    required_fields = []
    can_create = False
    can_update = False

class ChangeOrderCharges(BaseEntity):
    endpoint = "ChangeOrderCharges"
    display_fields = ["id", "ticketID", "name"]
    required_fields = ["ticketID", "name"]

class ChangeRequestLinks(BaseEntity):
    endpoint = "ChangeRequestLinks"
    display_fields = ["id", "changeRequestTicketID", "problemOrIncidentTicketID"]
    required_fields = ["changeRequestTicketID", "problemOrIncidentTicketID"]

class ChecklistLibraries(BaseEntity):
    endpoint = "ChecklistLibraries"
    display_fields = ["id", "name", "isActive"]
    required_fields = ["name"]

class ChecklistLibraryChecklistItems(BaseEntity):
    endpoint = "ChecklistLibraryChecklistItems"
    display_fields = ["id", "checklistLibraryID", "itemName"]
    required_fields = ["checklistLibraryID", "itemName"]

class ClassificationIcons(BaseEntity):
    endpoint = "ClassificationIcons"
    display_fields = ["id", "name"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class ClientPortalUsers(BaseEntity):
    endpoint = "ClientPortalUsers"
    display_fields = ["id", "contactID", "userName"]
    required_fields = ["contactID"]

class ComanagedAssociations(BaseEntity):
    endpoint = "ComanagedAssociations"
    display_fields = ["id", "companyID", "partnerCompanyID"]
    required_fields = ["companyID"]

class Countries(BaseEntity):
    endpoint = "Countries"
    display_fields = ["id", "name", "countryCode", "isActive"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class Currencies(BaseEntity):
    endpoint = "Currencies"
    display_fields = ["id", "name", "currencyCode", "isActive"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class DeletedTaskActivityLogs(BaseEntity):
    endpoint = "DeletedTaskActivityLogs"
    display_fields = ["id", "taskID", "deletedByResourceID", "deletedDateTime"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class DeletedTicketActivityLogs(BaseEntity):
    endpoint = "DeletedTicketActivityLogs"
    display_fields = ["id", "ticketID", "deletedByResourceID", "deletedDateTime"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class DeletedTicketLogs(BaseEntity):
    endpoint = "DeletedTicketLogs"
    display_fields = ["id", "ticketID", "deletedByResourceID"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class Departments(BaseEntity):
    endpoint = "Departments"
    display_fields = ["id", "name", "number"]
    required_fields = ["name"]

class DomainRegistrars(BaseEntity):
    endpoint = "DomainRegistrars"
    display_fields = ["id", "configurationItemID"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class Holidays(BaseEntity):
    endpoint = "Holidays"
    display_fields = ["id", "holidayName", "holidayDate"]
    required_fields = ["holidayName", "holidayDate", "holidaySetID"]

class HolidaySets(BaseEntity):
    endpoint = "HolidaySets"
    display_fields = ["id", "holidaySetName"]
    required_fields = ["holidaySetName"]

class InternalLocations(BaseEntity):
    endpoint = "InternalLocations"
    display_fields = ["id", "name", "isActive"]
    required_fields = ["name"]

class InternalLocationWithBusinessHours(BaseEntity):
    endpoint = "InternalLocationWithBusinessHours"
    display_fields = ["id", "name"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class Modules(BaseEntity):
    endpoint = "Modules"
    display_fields = ["id", "name", "isActive"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class NotificationHistory(BaseEntity):
    endpoint = "NotificationHistory"
    display_fields = ["id", "notificationDateTime", "templateName", "entityTitle"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class OrganizationalLevel1(BaseEntity):
    endpoint = "OrganizationalLevel1"
    display_fields = ["id", "name", "isActive"]
    required_fields = ["name"]

class OrganizationalLevel2(BaseEntity):
    endpoint = "OrganizationalLevel2"
    display_fields = ["id", "name", "isActive"]
    required_fields = ["name"]

class OrganizationalLevelAssociations(BaseEntity):
    endpoint = "OrganizationalLevelAssociations"
    display_fields = ["id", "resourceID", "organizationalLevel1ID"]
    required_fields = ["resourceID"]

class OrganizatonalResources(BaseEntity):
    endpoint = "OrganizatonalResources"
    display_fields = ["id", "resourceID"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class PaymentTerms(BaseEntity):
    endpoint = "PaymentTerms"
    display_fields = ["id", "name", "isActive"]
    required_fields = ["name"]

class ShippingTypes(BaseEntity):
    endpoint = "ShippingTypes"
    display_fields = ["id", "name", "isActive"]
    required_fields = ["name"]

class Skills(BaseEntity):
    endpoint = "Skills"
    display_fields = ["id", "name", "isActive"]
    required_fields = ["name"]

class SurveyResults(BaseEntity):
    endpoint = "SurveyResults"
    display_fields = ["id", "surveyID", "ticketID", "rating"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class Surveys(BaseEntity):
    endpoint = "Surveys"
    display_fields = ["id", "name", "isActive"]
    required_fields = ["name"]

class TagAliases(BaseEntity):
    endpoint = "TagAliases"
    display_fields = ["id", "tagID", "aliasName"]
    required_fields = ["tagID", "aliasName"]

class TagGroups(BaseEntity):
    endpoint = "TagGroups"
    display_fields = ["id", "name", "isActive"]
    required_fields = ["name"]

class Tags(BaseEntity):
    endpoint = "Tags"
    display_fields = ["id", "label", "isActive"]
    required_fields = ["label"]

class TaxCategories(BaseEntity):
    endpoint = "TaxCategories"
    display_fields = ["id", "name"]
    required_fields = ["name"]

class Taxes(BaseEntity):
    endpoint = "Taxes"
    display_fields = ["id", "taxName", "taxRate"]
    required_fields = ["taxName", "taxRegionID"]

class TaxRegions(BaseEntity):
    endpoint = "TaxRegions"
    display_fields = ["id", "name"]
    required_fields = ["name"]

class UserDefinedFieldDefinitions(BaseEntity):
    endpoint = "UserDefinedFieldDefinitions"
    display_fields = ["id", "name", "udfType", "dataType"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class UserDefinedFieldListItems(BaseEntity):
    endpoint = "UserDefinedFieldListItems"
    display_fields = ["id", "udfFieldID", "valueForDisplay"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class Version(BaseEntity):
    endpoint = "Version"
    display_fields = ["id", "versionNumber"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class WorkTypeModifiers(BaseEntity):
    endpoint = "WorkTypeModifiers"
    display_fields = ["id", "name", "isActive"]
    required_fields = ["name"]


# =============================================================================
# MASTER CATEGORY REGISTRY — drives the hierarchical CLI menu
# =============================================================================

ENTITY_CATEGORIES = {
    "Companies & CRM": {
        "Companies": Companies,
        "Company Alerts": CompanyAlerts,
        "Company Attachments": CompanyAttachments,
        "Company Categories": CompanyCategories,
        "Company Locations": CompanyLocations,
        "Company Notes": CompanyNotes,
        "Company Note Attachments": CompanyNoteAttachments,
        "Company Site Configurations": CompanySiteConfigurations,
        "Company Teams": CompanyTeams,
        "Company To-Dos": CompanyToDos,
    },
    "Contacts": {
        "Contacts": Contacts,
        "Contact Billing Product Assoc.": ContactBillingProductAssociations,
        "Contact Group Contacts": ContactGroupContacts,
        "Contact Groups": ContactGroups,
    },
    "Tickets & Service Desk": {
        "Tickets": Tickets,
        "Ticket Additional Config Items": TicketAdditionalConfigurationItems,
        "Ticket Additional Contacts": TicketAdditionalContacts,
        "Ticket Attachments": TicketAttachments,
        "Ticket Categories": TicketCategories,
        "Ticket Category Field Defaults": TicketCategoryFieldDefaults,
        "Ticket Change Request Approvals": TicketChangeRequestApprovals,
        "Ticket Charges": TicketCharges,
        "Ticket Checklist Items": TicketChecklistItems,
        "Ticket Checklist Libraries": TicketChecklistLibraries,
        "Ticket History": TicketHistory,
        "Ticket Notes": TicketNotes,
        "Ticket Note Attachments": TicketNoteAttachments,
        "Ticket RMA Credits": TicketRmaCredits,
        "Ticket Secondary Resources": TicketSecondaryResources,
        "Ticket Tag Associations": TicketTagAssociations,
    },
    "Projects & Tasks": {
        "Projects": Projects,
        "Project Attachments": ProjectAttachments,
        "Project Charges": ProjectCharges,
        "Project Notes": ProjectNotes,
        "Project Note Attachments": ProjectNoteAttachments,
        "Phases": Phases,
        "Tasks": Tasks,
        "Task Attachments": TaskAttachments,
        "Task Notes": TaskNotes,
        "Task Note Attachments": TaskNoteAttachments,
        "Task Predecessors": TaskPredecessors,
        "Task Secondary Resources": TaskSecondaryResources,
    },
    "Contracts": {
        "Contracts": Contracts,
        "Contract Billing Rules": ContractBillingRules,
        "Contract Block Hour Factors": ContractBlockHourFactors,
        "Contract Blocks": ContractBlocks,
        "Contract Charges": ContractCharges,
        "Contract Exclusion Billing Codes": ContractExclusionBillingCodes,
        "Contract Exclusion Roles": ContractExclusionRoles,
        "Contract Exclusion Sets": ContractExclusionSets,
        "Contract Excl. Set Excluded Roles": ContractExclusionSetExcludedRoles,
        "Contract Excl. Set Excluded WorkTypes": ContractExclusionSetExcludedWorkTypes,
        "Contract Milestones": ContractMilestones,
        "Contract Notes": ContractNotes,
        "Contract Note Attachments": ContractNoteAttachments,
        "Contract Rates": ContractRates,
        "Contract Retainers": ContractRetainers,
        "Contract Role Costs": ContractRoleCosts,
        "Contract Services": ContractServices,
        "Contract Service Adjustments": ContractServiceAdjustments,
        "Contract Service Bundles": ContractServiceBundles,
        "Contract Service Bundle Adj.": ContractServiceBundleAdjustments,
        "Contract Service Bundle Units": ContractServiceBundleUnits,
        "Contract Service Units": ContractServiceUnits,
        "Contract Ticket Purchases": ContractTicketPurchases,
    },
    "Configuration Items (Assets)": {
        "Configuration Items": ConfigurationItems,
        "Config Item Attachments": ConfigurationItemAttachments,
        "Config Item Billing Product Assoc.": ConfigurationItemBillingProductAssociations,
        "Config Item Categories": ConfigurationItemCategories,
        "Config Item Category UDF Assoc.": ConfigurationItemCategoryUdfAssociations,
        "Config Item DNS Records": ConfigurationItemDnsRecords,
        "Config Item Notes": ConfigurationItemNotes,
        "Config Item Note Attachments": ConfigurationItemNoteAttachments,
        "Config Item Related Items": ConfigurationItemRelatedItems,
        "Config Item SSL SAN": ConfigurationItemSslSubjectAlternativeName,
        "Config Item Types": ConfigurationItemTypes,
    },
    "Billing & Finance": {
        "Billing Codes": BillingCodes,
        "Billing Items": BillingItems,
        "Billing Item Approval Levels": BillingItemApprovalLevels,
        "Invoices": Invoices,
        "Invoice Templates": InvoiceTemplates,
        "Additional Invoice Field Values": AdditionalInvoiceFieldValues,
    },
    "Opportunities & Sales": {
        "Opportunities": Opportunities,
        "Opportunity Attachments": OpportunityAttachments,
        "Opportunity Categories": OpportunityCategories,
        "Sales Orders": SalesOrders,
        "Sales Order Attachments": SalesOrderAttachments,
        "Quotes": Quotes,
        "Quote Items": QuoteItems,
        "Quote Locations": QuoteLocations,
        "Quote Templates": QuoteTemplates,
    },
    "Resources & HR": {
        "Resources": Resources,
        "Resource Attachments": ResourceAttachments,
        "Resource Daily Availabilities": ResourceDailyAvailabilities,
        "Resource Roles": ResourceRoles,
        "Resource Role Departments": ResourceRoleDepartments,
        "Resource Role Queues": ResourceRoleQueues,
        "Resource Service Desk Roles": ResourceServiceDeskRoles,
        "Resource Skills": ResourceSkills,
        "Resource Time Off Balances": ResourceTimeOffBalances,
        "Resource Time Off Additional": ResourceTimeOffAdditional,
        "Resource Time Off Approvers": ResourceTimeOffApprovers,
        "Roles": Roles,
    },
    "Time & Expenses": {
        "Time Entries": TimeEntries,
        "Time Entry Attachments": TimeEntryAttachments,
        "Expense Items": ExpenseItems,
        "Expense Item Attachments": ExpenseItemAttachments,
        "Expense Reports": ExpenseReports,
        "Expense Report Attachments": ExpenseReportAttachments,
        "Time Off Requests": TimeOffRequests,
        "Approve Time Off Request": TimeOffRequestsApprove,
        "Reject Time Off Request": TimeOffRequestsReject,
    },
    "Products & Inventory": {
        "Products": Products,
        "Product Notes": ProductNotes,
        "Product Tiers": ProductTiers,
        "Product Vendors": ProductVendors,
        "Inventory Items": InventoryItems,
        "Inventory Item Serial Numbers": InventoryItemSerialNumbers,
        "Inventory Locations": InventoryLocations,
        "Inventory Products": InventoryProducts,
        "Inventory Stocked Items": InventoryStockedItems,
        "Add Stocked Items": InventoryStockedItemsAdd,
        "Remove Stocked Items": InventoryStockedItemsRemove,
        "Transfer Stocked Items": InventoryStockedItemsTransfer,
        "Inventory Transfers": InventoryTransfers,
    },
    "Knowledgebase & Articles": {
        "KB Articles": KnowledgeBaseArticles,
        "KB Categories": KnowledgeBaseCategories,
        "Article Attachments": ArticleAttachments,
        "Article Config Item Category Assoc.": ArticleConfigurationItemCategoryAssociations,
        "Article Notes": ArticleNotes,
        "Article Plain Text Content": ArticlePlainTextContent,
        "Article Tag Associations": ArticleTagAssociations,
        "Article Ticket Associations": ArticleTicketAssociations,
        "Article-to-Article Associations": ArticleToArticleAssociations,
        "Article-to-Document Associations": ArticleToDocumentAssociations,
    },
    "Documents": {
        "Documents": Documents,
        "Document Attachments": DocumentAttachments,
        "Document Categories": DocumentCategories,
        "Document Checklist Items": DocumentChecklistItems,
        "Document Checklist Libraries": DocumentChecklistLibraries,
        "Document Config Item Assoc.": DocumentConfigurationItemAssociations,
        "Document Config Item Category Assoc.": DocumentConfigurationItemCategoryAssociations,
        "Document Notes": DocumentNotes,
        "Document Tag Associations": DocumentTagAssociations,
        "Document Ticket Associations": DocumentTicketAssociations,
        "Document-to-Article Associations": DocumentToArticleAssociations,
    },
    "Service Calls": {
        "Service Calls": ServiceCalls,
        "Service Call Tasks": ServiceCallTasks,
        "Service Call Task Resources": ServiceCallTaskResources,
        "Service Call Tickets": ServiceCallTickets,
        "Service Call Ticket Resources": ServiceCallTicketResources,
    },
    "Services & Subscriptions": {
        "Services": Services,
        "Service Bundles": ServiceBundles,
        "Service Bundle Services": ServiceBundleServices,
        "Subscriptions": Subscriptions,
        "Subscription Periods": SubscriptionPeriods,
        "SLA Results": ServiceLevelAgreementResults,
    },
    "Purchase Orders": {
        "Purchase Orders": PurchaseOrders,
        "Purchase Order Items": PurchaseOrderItems,
        "Purchase Order Item Receiving": PurchaseOrderItemReceiving,
        "Purchase Approvals": PurchaseApprovals,
    },
    "Pricing": {
        "Price List Material Codes": PriceListMaterialCodes,
        "Price List Products": PriceListProducts,
        "Price List Product Tiers": PriceListProductTiers,
        "Price List Roles": PriceListRoles,
        "Price List Services": PriceListServices,
        "Price List Service Bundles": PriceListServiceBundles,
        "Price List Work Type Modifiers": PriceListWorkTypeModifiers,
    },
    "Admin & System": {
        "Action Types": ActionTypes,
        "Appointments": Appointments,
        "Attachment Info": AttachmentInfo,
        "Change Order Charges": ChangeOrderCharges,
        "Change Request Links": ChangeRequestLinks,
        "Checklist Libraries": ChecklistLibraries,
        "Checklist Library Items": ChecklistLibraryChecklistItems,
        "Classification Icons": ClassificationIcons,
        "Client Portal Users": ClientPortalUsers,
        "Co-managed Associations": ComanagedAssociations,
        "Countries": Countries,
        "Currencies": Currencies,
        "Deleted Task Activity Logs": DeletedTaskActivityLogs,
        "Deleted Ticket Activity Logs": DeletedTicketActivityLogs,
        "Deleted Ticket Logs": DeletedTicketLogs,
        "Departments": Departments,
        "Domain Registrars": DomainRegistrars,
        "Holidays": Holidays,
        "Holiday Sets": HolidaySets,
        "Internal Locations": InternalLocations,
        "Internal Location w/ Business Hours": InternalLocationWithBusinessHours,
        "Modules": Modules,
        "Notification History": NotificationHistory,
        "Organizational Level 1": OrganizationalLevel1,
        "Organizational Level 2": OrganizationalLevel2,
        "Organizational Level Associations": OrganizationalLevelAssociations,
        "Organizational Resources": OrganizatonalResources,
        "Payment Terms": PaymentTerms,
        "Shipping Types": ShippingTypes,
        "Skills": Skills,
        "Survey Results": SurveyResults,
        "Surveys": Surveys,
        "Tag Aliases": TagAliases,
        "Tag Groups": TagGroups,
        "Tags": Tags,
        "Tax Categories": TaxCategories,
        "Taxes": Taxes,
        "Tax Regions": TaxRegions,
        "UDF Definitions": UserDefinedFieldDefinitions,
        "UDF List Items": UserDefinedFieldListItems,
        "Version": Version,
        "Work Type Modifiers": WorkTypeModifiers,
    },
}
