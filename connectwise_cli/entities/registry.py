from .base import BaseEntity

# =============================================================================
# CATEGORY 1: Company & CRM
# =============================================================================

class Companies(BaseEntity):
    endpoint = "company/companies"
    display_fields = ["id", "name", "identifier", "status"]
    required_fields = ["name", "identifier"]

class CompanyContacts(BaseEntity):
    endpoint = "company/contacts"
    display_fields = ["id", "firstName", "lastName", "company/id"]
    required_fields = ["firstName", "lastName"]

class CompanyNotes(BaseEntity):
    endpoint = "company/companies/{parentId}/notes"
    display_fields = ["id", "text", "type/id"]
    required_fields = ["text"]
    parent_endpoint = "company/companies"
    parent_id_field = "parentId"

class CompanySites(BaseEntity):
    endpoint = "company/companies/{parentId}/sites"
    display_fields = ["id", "name", "city", "stateReference/name"]
    required_fields = ["name"]
    parent_endpoint = "company/companies"
    parent_id_field = "parentId"

class CompanyStatuses(BaseEntity):
    endpoint = "company/companies/statuses"
    display_fields = ["id", "name", "defaultFlag"]
    required_fields = ["name"]

class CompanyTypes(BaseEntity):
    endpoint = "company/companies/types"
    display_fields = ["id", "name"]
    required_fields = ["name"]

class CompanyTeams(BaseEntity):
    endpoint = "company/companies/{parentId}/teams"
    display_fields = ["id", "company/id", "teamRole/name"]
    required_fields = ["company", "teamRole"]
    parent_endpoint = "company/companies"
    parent_id_field = "parentId"

class CompanyGroups(BaseEntity):
    endpoint = "company/companies/{parentId}/groups"
    display_fields = ["id", "group/name"]
    required_fields = ["group"]
    parent_endpoint = "company/companies"
    parent_id_field = "parentId"

class CompanyManagementSummary(BaseEntity):
    endpoint = "company/companies/{parentId}/managementSummary"
    display_fields = ["id", "managementSolution/name"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False
    parent_endpoint = "company/companies"
    parent_id_field = "parentId"

class CompanyTypeAssociations(BaseEntity):
    endpoint = "company/companies/{parentId}/typeAssociations"
    display_fields = ["id", "type/name"]
    required_fields = ["type"]
    parent_endpoint = "company/companies"
    parent_id_field = "parentId"

class ContactTypes(BaseEntity):
    endpoint = "company/contacts/types"
    display_fields = ["id", "description"]
    required_fields = ["description"]

class ContactDepartments(BaseEntity):
    endpoint = "company/contacts/departments"
    display_fields = ["id", "name"]
    required_fields = ["name"]

class ContactRelationships(BaseEntity):
    endpoint = "company/contacts/relationships"
    display_fields = ["id", "name"]
    required_fields = ["name"]

class ContactCommunications(BaseEntity):
    endpoint = "company/contacts/{parentId}/communications"
    display_fields = ["id", "type/name", "value", "defaultFlag"]
    required_fields = ["type", "value"]
    parent_endpoint = "company/contacts"
    parent_id_field = "parentId"

class ContactNotes(BaseEntity):
    endpoint = "company/contacts/{parentId}/notes"
    display_fields = ["id", "text", "type/id"]
    required_fields = ["text"]
    parent_endpoint = "company/contacts"
    parent_id_field = "parentId"

class ContactTracks(BaseEntity):
    endpoint = "company/contacts/{parentId}/tracks"
    display_fields = ["id", "track/name"]
    required_fields = ["track"]
    parent_endpoint = "company/contacts"
    parent_id_field = "parentId"

class Configurations(BaseEntity):
    endpoint = "company/configurations"
    display_fields = ["id", "name", "company/name", "type/name"]
    required_fields = ["name", "company", "type"]

class ConfigurationStatuses(BaseEntity):
    endpoint = "company/configurations/statuses"
    display_fields = ["id", "description", "closedFlag"]
    required_fields = ["description"]

class ConfigurationTypes(BaseEntity):
    endpoint = "company/configurations/types"
    display_fields = ["id", "name", "inactiveFlag"]
    required_fields = ["name"]

class CompanyPickerItems(BaseEntity):
    endpoint = "company/companyPickerItems"
    display_fields = ["id", "member/name", "company/name"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class ManagementBackups(BaseEntity):
    endpoint = "company/managementBackups"
    display_fields = ["id", "managedIdentifier/name"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class Tracks(BaseEntity):
    endpoint = "company/tracks"
    display_fields = ["id", "name", "inactiveFlag"]
    required_fields = ["name"]

class TrackActions(BaseEntity):
    endpoint = "company/tracks/{parentId}/actions"
    display_fields = ["id", "notifyType/name", "daysToExecute"]
    required_fields = ["notifyType"]
    parent_endpoint = "company/tracks"
    parent_id_field = "parentId"

class PortalConfigurations(BaseEntity):
    endpoint = "company/portalConfigurations"
    display_fields = ["id", "name", "url"]
    required_fields = ["name"]

class CompanyFinances(BaseEntity):
    endpoint = "company/companies/{parentId}/finances"
    display_fields = ["id", "company/id"]
    required_fields = []
    can_create = False
    can_delete = False
    parent_endpoint = "company/companies"
    parent_id_field = "parentId"


# =============================================================================
# CATEGORY 2: Service Desk
# =============================================================================

class ServiceTickets(BaseEntity):
    endpoint = "service/tickets"
    display_fields = ["id", "summary", "status/name", "priority/name"]
    required_fields = ["summary", "company", "board"]

class ServiceBoards(BaseEntity):
    endpoint = "service/boards"
    display_fields = ["id", "name", "inactiveFlag"]
    required_fields = ["name"]

class BoardStatuses(BaseEntity):
    endpoint = "service/boards/{parentId}/statuses"
    display_fields = ["id", "name", "sortOrder", "closedStatus"]
    required_fields = ["name"]
    parent_endpoint = "service/boards"
    parent_id_field = "parentId"

class BoardTypes(BaseEntity):
    endpoint = "service/boards/{parentId}/types"
    display_fields = ["id", "name", "inactiveFlag"]
    required_fields = ["name"]
    parent_endpoint = "service/boards"
    parent_id_field = "parentId"

class BoardSubTypes(BaseEntity):
    endpoint = "service/boards/{parentId}/subtypes"
    display_fields = ["id", "name", "inactiveFlag"]
    required_fields = ["name"]
    parent_endpoint = "service/boards"
    parent_id_field = "parentId"

class BoardItems(BaseEntity):
    endpoint = "service/boards/{parentId}/items"
    display_fields = ["id", "name", "inactiveFlag"]
    required_fields = ["name"]
    parent_endpoint = "service/boards"
    parent_id_field = "parentId"

class BoardTeams(BaseEntity):
    endpoint = "service/boards/{parentId}/teams"
    display_fields = ["id", "name", "teamRole/name"]
    required_fields = ["name"]
    parent_endpoint = "service/boards"
    parent_id_field = "parentId"

class BoardAutoAssignResources(BaseEntity):
    endpoint = "service/boards/{parentId}/autoAssignResources"
    display_fields = ["id", "member/name"]
    required_fields = ["member"]
    parent_endpoint = "service/boards"
    parent_id_field = "parentId"

class BoardExcludedMembers(BaseEntity):
    endpoint = "service/boards/{parentId}/excludedMembers"
    display_fields = ["id", "member/name"]
    required_fields = ["member"]
    parent_endpoint = "service/boards"
    parent_id_field = "parentId"

class BoardNotifications(BaseEntity):
    endpoint = "service/boards/{parentId}/notifications"
    display_fields = ["id", "member/name", "notifyType"]
    required_fields = ["member", "notifyType"]
    parent_endpoint = "service/boards"
    parent_id_field = "parentId"

class BoardTypeSubTypeItemAssociations(BaseEntity):
    endpoint = "service/boards/{parentId}/typeSubTypeItemAssociations"
    display_fields = ["id", "type/name", "subType/name"]
    required_fields = ["type"]
    parent_endpoint = "service/boards"
    parent_id_field = "parentId"

class TicketNotes(BaseEntity):
    endpoint = "service/tickets/{parentId}/notes"
    display_fields = ["id", "text", "internalAnalysisFlag", "detailDescriptionFlag"]
    required_fields = ["text"]
    parent_endpoint = "service/tickets"
    parent_id_field = "parentId"

class TicketTasks(BaseEntity):
    endpoint = "service/tickets/{parentId}/tasks"
    display_fields = ["id", "notes", "priority"]
    required_fields = ["notes"]
    parent_endpoint = "service/tickets"
    parent_id_field = "parentId"

class TicketTimeEntries(BaseEntity):
    endpoint = "service/tickets/{parentId}/timeentries"
    display_fields = ["id", "member/name", "timeStart", "timeEnd"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False
    parent_endpoint = "service/tickets"
    parent_id_field = "parentId"

class TicketScheduleEntries(BaseEntity):
    endpoint = "service/tickets/{parentId}/scheduleentries"
    display_fields = ["id", "member/name", "dateStart", "dateEnd"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False
    parent_endpoint = "service/tickets"
    parent_id_field = "parentId"

class TicketDocuments(BaseEntity):
    endpoint = "service/tickets/{parentId}/documents"
    display_fields = ["id", "title", "fileName"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False
    parent_endpoint = "service/tickets"
    parent_id_field = "parentId"

class TicketConfigurations(BaseEntity):
    endpoint = "service/tickets/{parentId}/configurations"
    display_fields = ["id", "configuration/name"]
    required_fields = ["configuration"]
    parent_endpoint = "service/tickets"
    parent_id_field = "parentId"

class TicketMerge(BaseEntity):
    endpoint = "service/tickets/{parentId}/merge"
    display_fields = ["id"]
    required_fields = ["mergeTicketIds"]
    can_update = False
    can_delete = False
    parent_endpoint = "service/tickets"
    parent_id_field = "parentId"

class Priorities(BaseEntity):
    endpoint = "service/priorities"
    display_fields = ["id", "name", "sortOrder", "defaultFlag"]
    required_fields = ["name"]

class ServiceSources(BaseEntity):
    endpoint = "service/sources"
    display_fields = ["id", "name", "defaultFlag"]
    required_fields = ["name"]

class Impacts(BaseEntity):
    endpoint = "service/impacts"
    display_fields = ["id", "name", "defaultFlag"]
    required_fields = ["name"]
    can_delete = False

class Severities(BaseEntity):
    endpoint = "service/severities"
    display_fields = ["id", "name", "defaultFlag"]
    required_fields = ["name"]
    can_delete = False

class SLAs(BaseEntity):
    endpoint = "service/SLAs"
    display_fields = ["id", "name", "defaultFlag"]
    required_fields = ["name"]

class SLAPriorities(BaseEntity):
    endpoint = "service/SLAs/{parentId}/priorities"
    display_fields = ["id", "priority/name", "respondHours", "planWithin"]
    required_fields = ["priority"]
    parent_endpoint = "service/SLAs"
    parent_id_field = "parentId"

class KnowledgeBaseArticles(BaseEntity):
    endpoint = "service/knowledgeBaseArticles"
    display_fields = ["id", "title", "boardId"]
    required_fields = ["title"]

class ServiceSurveys(BaseEntity):
    endpoint = "service/surveys"
    display_fields = ["id", "name", "inactiveFlag"]
    required_fields = ["name"]

class ServiceCodeAssociations(BaseEntity):
    endpoint = "service/codes"
    display_fields = ["id", "name"]
    required_fields = ["name"]

class ServiceLocations(BaseEntity):
    endpoint = "service/locations"
    display_fields = ["id", "name", "where"]
    required_fields = ["name"]

class ServiceSignoffs(BaseEntity):
    endpoint = "service/serviceSignoff"
    display_fields = ["id", "name", "defaultFlag"]
    required_fields = ["name"]

class ServiceTemplates(BaseEntity):
    endpoint = "service/templates"
    display_fields = ["id", "name", "board/name"]
    required_fields = ["name", "board"]
    can_delete = False


# =============================================================================
# CATEGORY 3: Sales
# =============================================================================

class Opportunities(BaseEntity):
    endpoint = "sales/opportunities"
    display_fields = ["id", "name", "company/id", "status"]
    required_fields = ["name", "company"]

class OpportunityStatuses(BaseEntity):
    endpoint = "sales/opportunities/statuses"
    display_fields = ["id", "name", "defaultFlag", "closedFlag"]
    required_fields = ["name"]

class OpportunityTypes(BaseEntity):
    endpoint = "sales/opportunities/types"
    display_fields = ["id", "description", "inactiveFlag"]
    required_fields = ["description"]

class OpportunityNotes(BaseEntity):
    endpoint = "sales/opportunities/{parentId}/notes"
    display_fields = ["id", "text", "type/name"]
    required_fields = ["text"]
    parent_endpoint = "sales/opportunities"
    parent_id_field = "parentId"

class OpportunityForecasts(BaseEntity):
    endpoint = "sales/opportunities/{parentId}/forecast"
    display_fields = ["id", "revenue", "cost"]
    required_fields = ["status", "forecastType"]
    parent_endpoint = "sales/opportunities"
    parent_id_field = "parentId"

class OpportunityContacts(BaseEntity):
    endpoint = "sales/opportunities/{parentId}/contacts"
    display_fields = ["id", "contact/name", "role/name"]
    required_fields = ["contact"]
    parent_endpoint = "sales/opportunities"
    parent_id_field = "parentId"

class OpportunityTeams(BaseEntity):
    endpoint = "sales/opportunities/{parentId}/team"
    display_fields = ["id", "member/name", "salesTeam"]
    required_fields = ["member"]
    parent_endpoint = "sales/opportunities"
    parent_id_field = "parentId"

class OpportunityRatings(BaseEntity):
    endpoint = "sales/opportunities/ratings"
    display_fields = ["id", "name", "sortOrder"]
    required_fields = ["name"]

class Probabilities(BaseEntity):
    endpoint = "sales/probabilities"
    display_fields = ["id", "probability"]
    required_fields = ["probability"]

class Stages(BaseEntity):
    endpoint = "sales/stages"
    display_fields = ["id", "name", "probability/name"]
    required_fields = ["name"]

class Activities(BaseEntity):
    endpoint = "sales/activities"
    display_fields = ["id", "name", "company/name", "status"]
    required_fields = ["name"]

class ActivityStatuses(BaseEntity):
    endpoint = "sales/activities/statuses"
    display_fields = ["id", "name", "defaultFlag", "closedFlag"]
    required_fields = ["name"]

class ActivityTypes(BaseEntity):
    endpoint = "sales/activities/types"
    display_fields = ["id", "name", "inactiveFlag"]
    required_fields = ["name"]

class Orders(BaseEntity):
    endpoint = "sales/orders"
    display_fields = ["id", "opportunity/id", "status"]
    required_fields = ["opportunity"]

class OrderStatuses(BaseEntity):
    endpoint = "sales/orders/statuses"
    display_fields = ["id", "name", "defaultFlag", "closedFlag"]
    required_fields = ["name"]

class SalesRoles(BaseEntity):
    endpoint = "sales/roles"
    display_fields = ["id", "name", "sortOrder"]
    required_fields = ["name"]

class SalesTeams(BaseEntity):
    endpoint = "sales/salesTeams"
    display_fields = ["id", "salesTeamDescription", "inactiveFlag"]
    required_fields = ["salesTeamDescription"]

class Commissions(BaseEntity):
    endpoint = "sales/commissions"
    display_fields = ["id", "member/name", "commissionPercent"]
    required_fields = ["member", "commissionPercent"]

class SalesQuotas(BaseEntity):
    endpoint = "sales/quotas"
    display_fields = ["id", "member/name", "forecastYear", "forecastRevenue"]
    required_fields = ["forecastYear"]


# =============================================================================
# CATEGORY 4: Finance & Billing
# =============================================================================

class Agreements(BaseEntity):
    endpoint = "finance/agreements"
    display_fields = ["id", "name", "company/name", "type/name"]
    required_fields = ["name", "company", "type"]

class AgreementTypes(BaseEntity):
    endpoint = "finance/agreements/types"
    display_fields = ["id", "name", "inactiveFlag"]
    required_fields = ["name"]

class AgreementAdditions(BaseEntity):
    endpoint = "finance/agreements/{parentId}/additions"
    display_fields = ["id", "product/description", "quantity"]
    required_fields = ["product"]
    parent_endpoint = "finance/agreements"
    parent_id_field = "parentId"

class AgreementAdjustments(BaseEntity):
    endpoint = "finance/agreements/{parentId}/adjustments"
    display_fields = ["id", "description", "amount"]
    required_fields = ["description"]
    parent_endpoint = "finance/agreements"
    parent_id_field = "parentId"

class AgreementBoardDefaults(BaseEntity):
    endpoint = "finance/agreements/{parentId}/boardDefaults"
    display_fields = ["id", "board/name", "serviceType/name"]
    required_fields = ["board"]
    parent_endpoint = "finance/agreements"
    parent_id_field = "parentId"

class AgreementSites(BaseEntity):
    endpoint = "finance/agreements/{parentId}/sites"
    display_fields = ["id", "site/name", "company/name"]
    required_fields = ["company", "site"]
    parent_endpoint = "finance/agreements"
    parent_id_field = "parentId"

class AgreementWorkRoleExclusions(BaseEntity):
    endpoint = "finance/agreements/{parentId}/workRoleExclusions"
    display_fields = ["id", "workRole/name"]
    required_fields = ["workRole"]
    parent_endpoint = "finance/agreements"
    parent_id_field = "parentId"

class AgreementWorkTypeExclusions(BaseEntity):
    endpoint = "finance/agreements/{parentId}/workTypeExclusions"
    display_fields = ["id", "workType/name"]
    required_fields = ["workType"]
    parent_endpoint = "finance/agreements"
    parent_id_field = "parentId"

class AgreementWorkRoles(BaseEntity):
    endpoint = "finance/agreements/{parentId}/workRoles"
    display_fields = ["id", "workRole/name", "rate"]
    required_fields = ["workRole"]
    parent_endpoint = "finance/agreements"
    parent_id_field = "parentId"

class AgreementWorkTypes(BaseEntity):
    endpoint = "finance/agreements/{parentId}/workTypes"
    display_fields = ["id", "workType/name", "billTime"]
    required_fields = ["workType"]
    parent_endpoint = "finance/agreements"
    parent_id_field = "parentId"

class Invoices(BaseEntity):
    endpoint = "finance/invoices"
    display_fields = ["id", "invoiceNumber", "company/name", "total"]
    required_fields = []
    can_create = False
    can_delete = False

class InvoicePayments(BaseEntity):
    endpoint = "finance/invoices/{parentId}/payments"
    display_fields = ["id", "amount", "paymentDate"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False
    parent_endpoint = "finance/invoices"
    parent_id_field = "parentId"

class GLAccounts(BaseEntity):
    endpoint = "finance/glAccounts"
    display_fields = ["id", "glType", "mappedType/name"]
    required_fields = ["glType"]

class BillingCycles(BaseEntity):
    endpoint = "finance/billingCycles"
    display_fields = ["id", "name", "identifier"]
    required_fields = ["name", "identifier"]

class BillingSetups(BaseEntity):
    endpoint = "finance/billingSetups"
    display_fields = ["id", "invoiceTitle", "emailTemplate/name"]
    required_fields = []
    can_create = False
    can_delete = False

class BillingTerms(BaseEntity):
    endpoint = "finance/billingTerms"
    display_fields = ["id", "name", "defaultFlag"]
    required_fields = ["name"]

class TaxCodes(BaseEntity):
    endpoint = "finance/taxCodes"
    display_fields = ["id", "identifier", "description", "defaultFlag"]
    required_fields = ["identifier", "description"]

class TaxCodeLevels(BaseEntity):
    endpoint = "finance/taxCodes/{parentId}/taxCodeLevels"
    display_fields = ["id", "taxLevel", "taxRate"]
    required_fields = ["taxLevel"]
    parent_endpoint = "finance/taxCodes"
    parent_id_field = "parentId"

class Currencies(BaseEntity):
    endpoint = "finance/currencies"
    display_fields = ["id", "currencyIdentifier", "name", "symbol"]
    required_fields = ["currencyIdentifier", "name"]

class DeliveryMethods(BaseEntity):
    endpoint = "finance/deliveryMethods"
    display_fields = ["id", "name", "defaultFlag"]
    required_fields = ["name"]

class AccountingBatches(BaseEntity):
    endpoint = "finance/accounting/batches"
    display_fields = ["id", "batchIdentifier", "closedFlag"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class AccountingUnpostedExpenses(BaseEntity):
    endpoint = "finance/accounting/unpostedexpenses"
    display_fields = ["id", "company/name", "description", "total"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class AccountingUnpostedInvoices(BaseEntity):
    endpoint = "finance/accounting/unpostedinvoices"
    display_fields = ["id", "company/name", "invoiceNumber", "total"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class AccountingUnpostedProcurements(BaseEntity):
    endpoint = "finance/accounting/unpostedprocurement"
    display_fields = ["id", "description", "total"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False


# =============================================================================
# CATEGORY 5: Project
# =============================================================================

class Projects(BaseEntity):
    endpoint = "project/projects"
    display_fields = ["id", "name", "company/name", "status/name"]
    required_fields = ["name", "board", "company"]

class ProjectPhases(BaseEntity):
    endpoint = "project/projects/{parentId}/phases"
    display_fields = ["id", "description", "wbsCode"]
    required_fields = ["description"]
    parent_endpoint = "project/projects"
    parent_id_field = "parentId"

class ProjectNotes(BaseEntity):
    endpoint = "project/projects/{parentId}/notes"
    display_fields = ["id", "text", "type/name"]
    required_fields = ["text"]
    parent_endpoint = "project/projects"
    parent_id_field = "parentId"

class ProjectTeamMembers(BaseEntity):
    endpoint = "project/projects/{parentId}/teamMembers"
    display_fields = ["id", "member/name", "workRole/name"]
    required_fields = ["member"]
    parent_endpoint = "project/projects"
    parent_id_field = "parentId"

class ProjectContacts(BaseEntity):
    endpoint = "project/projectContacts"
    display_fields = ["id", "contact/name", "project/name"]
    required_fields = ["contact", "project"]

class ProjectStatuses(BaseEntity):
    endpoint = "project/statuses"
    display_fields = ["id", "name", "defaultFlag", "closedFlag"]
    required_fields = ["name"]

class ProjectBoards(BaseEntity):
    endpoint = "project/boards"
    display_fields = ["id", "name", "inactiveFlag"]
    required_fields = ["name"]

class ProjectBoardTeamMembers(BaseEntity):
    endpoint = "project/boards/{parentId}/teamMembers"
    display_fields = ["id", "member/name", "workRole/name"]
    required_fields = ["member"]
    parent_endpoint = "project/boards"
    parent_id_field = "parentId"

class ProjectSecurityRoles(BaseEntity):
    endpoint = "project/securityRoles"
    display_fields = ["id", "name"]
    required_fields = ["name"]

class ProjectTickets(BaseEntity):
    endpoint = "project/tickets"
    display_fields = ["id", "summary", "project/name"]
    required_fields = ["summary", "project"]


# =============================================================================
# CATEGORY 6: Time & Expense
# =============================================================================

class TimeEntries(BaseEntity):
    endpoint = "time/entries"
    display_fields = ["id", "member/name", "timeStart", "timeEnd", "actualHours"]
    required_fields = ["member", "timeStart", "timeEnd"]

class TimeSheets(BaseEntity):
    endpoint = "time/sheets"
    display_fields = ["id", "member/name", "year", "period"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class TimeAccruals(BaseEntity):
    endpoint = "time/accruals"
    display_fields = ["id", "member/name", "vacationAvailableHours"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class TimePeriodSetups(BaseEntity):
    endpoint = "time/timePeriodSetups"
    display_fields = ["id", "type", "periodApplyTo"]
    required_fields = []
    can_create = False
    can_delete = False

class ExpenseEntries(BaseEntity):
    endpoint = "expense/entries"
    display_fields = ["id", "member/name", "company/name", "amount"]
    required_fields = ["company", "chargeToId", "chargeToType"]

class ExpenseReports(BaseEntity):
    endpoint = "expense/reports"
    display_fields = ["id", "member/name", "year", "period", "total"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class ExpenseTypes(BaseEntity):
    endpoint = "expense/types"
    display_fields = ["id", "name", "inactiveFlag"]
    required_fields = ["name"]

class ExpensePaymentTypes(BaseEntity):
    endpoint = "expense/paymentTypes"
    display_fields = ["id", "name", "defaultFlag"]
    required_fields = ["name"]

class ExpenseClassifications(BaseEntity):
    endpoint = "expense/classifications"
    display_fields = ["id", "name", "defaultFlag"]
    required_fields = ["name"]

class ChargeCodes(BaseEntity):
    endpoint = "time/chargeCodes"
    display_fields = ["id", "name", "company/name"]
    required_fields = ["name"]

class WorkRoles(BaseEntity):
    endpoint = "time/workRoles"
    display_fields = ["id", "name", "inactiveFlag", "hourlyRate"]
    required_fields = ["name"]

class WorkTypes(BaseEntity):
    endpoint = "time/workTypes"
    display_fields = ["id", "name", "inactiveFlag", "billTime"]
    required_fields = ["name"]


# =============================================================================
# CATEGORY 7: Procurement
# =============================================================================

class CatalogItems(BaseEntity):
    endpoint = "procurement/catalog"
    display_fields = ["id", "identifier", "description", "price"]
    required_fields = ["identifier", "description"]

class CatalogComponents(BaseEntity):
    endpoint = "procurement/catalog/{parentId}/components"
    display_fields = ["id", "catalogItem/description", "quantity"]
    required_fields = ["catalogItem", "quantity"]
    parent_endpoint = "procurement/catalog"
    parent_id_field = "parentId"

class Categories(BaseEntity):
    endpoint = "procurement/categories"
    display_fields = ["id", "name", "inactiveFlag"]
    required_fields = ["name"]

class SubCategories(BaseEntity):
    endpoint = "procurement/categories/{parentId}/subcategories"
    display_fields = ["id", "name", "inactiveFlag"]
    required_fields = ["name"]
    parent_endpoint = "procurement/categories"
    parent_id_field = "parentId"

class ProductTypes(BaseEntity):
    endpoint = "procurement/types"
    display_fields = ["id", "name", "inactiveFlag"]
    required_fields = ["name"]

class Manufacturers(BaseEntity):
    endpoint = "procurement/manufacturers"
    display_fields = ["id", "name", "inactiveFlag"]
    required_fields = ["name"]

class PurchaseOrders(BaseEntity):
    endpoint = "procurement/purchaseorders"
    display_fields = ["id", "vendorCompany/name", "status/name", "total"]
    required_fields = ["vendorCompany"]

class PurchaseOrderLineItems(BaseEntity):
    endpoint = "procurement/purchaseorders/{parentId}/lineitems"
    display_fields = ["id", "description", "quantity", "unitCost"]
    required_fields = ["description"]
    parent_endpoint = "procurement/purchaseorders"
    parent_id_field = "parentId"

class PurchaseOrderStatuses(BaseEntity):
    endpoint = "procurement/purchaseorderstatuses"
    display_fields = ["id", "name", "defaultFlag", "closedFlag"]
    required_fields = ["name"]

class ProductComponents(BaseEntity):
    endpoint = "procurement/products"
    display_fields = ["id", "catalogItem/description", "quantity"]
    required_fields = ["catalogItem"]

class Warehouses(BaseEntity):
    endpoint = "procurement/warehouses"
    display_fields = ["id", "name", "company/name"]
    required_fields = ["name", "company"]

class WarehouseBins(BaseEntity):
    endpoint = "procurement/warehouses/{parentId}/bins"
    display_fields = ["id", "name", "defaultFlag"]
    required_fields = ["name"]
    parent_endpoint = "procurement/warehouses"
    parent_id_field = "parentId"

class RMAs(BaseEntity):
    endpoint = "procurement/RMADispositions"
    display_fields = ["id", "name", "defaultFlag"]
    required_fields = ["name"]

class ShipmentMethods(BaseEntity):
    endpoint = "procurement/shipmentmethods"
    display_fields = ["id", "name", "defaultFlag"]
    required_fields = ["name"]

class UnitOfMeasures(BaseEntity):
    endpoint = "procurement/unitOfMeasures"
    display_fields = ["id", "name", "inactiveFlag"]
    required_fields = ["name"]

class PricingSchedules(BaseEntity):
    endpoint = "procurement/pricingschedules"
    display_fields = ["id", "name", "defaultFlag", "inactiveFlag"]
    required_fields = ["name"]

class Adjustments(BaseEntity):
    endpoint = "procurement/adjustments"
    display_fields = ["id", "identifier", "type/name"]
    required_fields = ["identifier", "type"]

class AdjustmentDetails(BaseEntity):
    endpoint = "procurement/adjustments/{parentId}/details"
    display_fields = ["id", "catalogItem/description", "quantityAdjusted"]
    required_fields = ["catalogItem"]
    parent_endpoint = "procurement/adjustments"
    parent_id_field = "parentId"


# =============================================================================
# CATEGORY 8: Marketing
# =============================================================================

class Campaigns(BaseEntity):
    endpoint = "marketing/campaigns"
    display_fields = ["id", "name", "type/name", "status/name"]
    required_fields = ["name", "type"]

class CampaignStatuses(BaseEntity):
    endpoint = "marketing/campaigns/statuses"
    display_fields = ["id", "name", "defaultFlag"]
    required_fields = ["name"]

class CampaignTypes(BaseEntity):
    endpoint = "marketing/campaigns/types"
    display_fields = ["id", "name", "defaultFlag"]
    required_fields = ["name"]

class CampaignSubTypes(BaseEntity):
    endpoint = "marketing/campaigns/subTypes"
    display_fields = ["id", "name", "typeId"]
    required_fields = ["name"]

class CampaignAudits(BaseEntity):
    endpoint = "marketing/campaigns/{parentId}/audits"
    display_fields = ["id", "member/name", "dateCreated"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False
    parent_endpoint = "marketing/campaigns"
    parent_id_field = "parentId"

class CampaignEmailsOpened(BaseEntity):
    endpoint = "marketing/campaigns/{parentId}/emailsOpened"
    display_fields = ["id", "contact/name", "dateOpened"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False
    parent_endpoint = "marketing/campaigns"
    parent_id_field = "parentId"

class CampaignFormsSubmitted(BaseEntity):
    endpoint = "marketing/campaigns/{parentId}/formsSubmitted"
    display_fields = ["id", "contact/name", "dateSubmitted"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False
    parent_endpoint = "marketing/campaigns"
    parent_id_field = "parentId"

class CampaignLinksClicked(BaseEntity):
    endpoint = "marketing/campaigns/{parentId}/linksClicked"
    display_fields = ["id", "contact/name", "dateClicked"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False
    parent_endpoint = "marketing/campaigns"
    parent_id_field = "parentId"

class Groups(BaseEntity):
    endpoint = "marketing/groups"
    display_fields = ["id", "name", "description"]
    required_fields = ["name"]

class GroupCompanies(BaseEntity):
    endpoint = "marketing/groups/{parentId}/companies"
    display_fields = ["id", "company/name"]
    required_fields = ["company"]
    parent_endpoint = "marketing/groups"
    parent_id_field = "parentId"

class GroupContacts(BaseEntity):
    endpoint = "marketing/groups/{parentId}/contacts"
    display_fields = ["id", "contact/name"]
    required_fields = ["contact"]
    parent_endpoint = "marketing/groups"
    parent_id_field = "parentId"


# =============================================================================
# CATEGORY 9: Schedule
# =============================================================================

class ScheduleEntries(BaseEntity):
    endpoint = "schedule/entries"
    display_fields = ["id", "member/name", "dateStart", "dateEnd", "type/name"]
    required_fields = ["member", "dateStart", "dateEnd", "type"]

class ScheduleStatuses(BaseEntity):
    endpoint = "schedule/statuses"
    display_fields = ["id", "name", "defaultFlag"]
    required_fields = ["name"]

class ScheduleTypes(BaseEntity):
    endpoint = "schedule/types"
    display_fields = ["id", "name", "identifier"]
    required_fields = ["name", "identifier"]

class ScheduleColors(BaseEntity):
    endpoint = "schedule/colors"
    display_fields = ["id", "name"]
    required_fields = ["name"]
    can_delete = False

class ScheduleReminderTimes(BaseEntity):
    endpoint = "schedule/reminderTimes"
    display_fields = ["id", "name", "defaultFlag"]
    required_fields = ["name"]
    can_delete = False

class Calendars(BaseEntity):
    endpoint = "schedule/calendars"
    display_fields = ["id", "name", "holidayList/name"]
    required_fields = ["name"]

class CalendarInfos(BaseEntity):
    endpoint = "schedule/calendars/{parentId}/info"
    display_fields = ["id", "calendar/name"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False
    parent_endpoint = "schedule/calendars"
    parent_id_field = "parentId"

class HolidayLists(BaseEntity):
    endpoint = "schedule/holidayLists"
    display_fields = ["id", "name"]
    required_fields = ["name"]

class Holidays(BaseEntity):
    endpoint = "schedule/holidayLists/{parentId}/holidays"
    display_fields = ["id", "name", "allDayFlag", "date"]
    required_fields = ["name", "date"]
    parent_endpoint = "schedule/holidayLists"
    parent_id_field = "parentId"

class SchedulePortalCalendars(BaseEntity):
    endpoint = "schedule/portalcalendars"
    display_fields = ["id", "description", "weekStart"]
    required_fields = []
    can_create = False
    can_delete = False


# =============================================================================
# CATEGORY 10: System & Admin
# =============================================================================

class Members(BaseEntity):
    endpoint = "system/members"
    display_fields = ["id", "identifier", "firstName", "lastName", "inactiveFlag"]
    required_fields = ["identifier", "firstName", "lastName"]
    can_delete = False

class MemberDeactivations(BaseEntity):
    endpoint = "system/members/{parentId}/deactivate"
    display_fields = ["id"]
    required_fields = []
    can_update = False
    can_delete = False
    parent_endpoint = "system/members"
    parent_id_field = "parentId"

class Callbacks(BaseEntity):
    endpoint = "system/callbacks"
    display_fields = ["id", "url", "objectId", "type"]
    required_fields = ["url", "objectId", "type"]

class AuditTrail(BaseEntity):
    endpoint = "system/audittrail"
    display_fields = ["id", "text", "enteredDate", "source"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class ConnectWiseHostedSetups(BaseEntity):
    endpoint = "system/connectwisehostedsetups"
    display_fields = ["id", "screenId", "description"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class Documents(BaseEntity):
    endpoint = "system/documents"
    display_fields = ["id", "title", "fileName"]
    required_fields = ["title"]

class DocumentTypes(BaseEntity):
    endpoint = "system/documents/types"
    display_fields = ["id", "name"]
    required_fields = ["name"]

class EmailConnectors(BaseEntity):
    endpoint = "system/emailConnectors"
    display_fields = ["id", "imapSetup/name", "emailErrors"]
    required_fields = []
    can_create = False
    can_delete = False

class SecurityRoles(BaseEntity):
    endpoint = "system/securityRoles"
    display_fields = ["id", "name"]
    required_fields = ["name"]

class Info(BaseEntity):
    endpoint = "system/info"
    display_fields = ["version", "isCloud"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class Departments(BaseEntity):
    endpoint = "system/departments"
    display_fields = ["id", "name"]
    required_fields = ["identifier", "name"]

class Locations(BaseEntity):
    endpoint = "system/locations"
    display_fields = ["id", "name", "where"]
    required_fields = ["name"]

class LocationDepartments(BaseEntity):
    endpoint = "system/locations/{parentId}/departments"
    display_fields = ["id", "department/name"]
    required_fields = ["department"]
    parent_endpoint = "system/locations"
    parent_id_field = "parentId"

class LocationWorkRoles(BaseEntity):
    endpoint = "system/locations/{parentId}/workRoles"
    display_fields = ["id", "workRole/name", "location/name"]
    required_fields = ["workRole", "location"]
    parent_endpoint = "system/locations"
    parent_id_field = "parentId"

class Workflows(BaseEntity):
    endpoint = "system/workflows"
    display_fields = ["id", "name", "tableName"]
    required_fields = ["name"]

class WorkflowActions(BaseEntity):
    endpoint = "system/workflows/{parentId}/actions"
    display_fields = ["id", "name", "actionType"]
    required_fields = ["name"]
    parent_endpoint = "system/workflows"
    parent_id_field = "parentId"

class WorkflowEvents(BaseEntity):
    endpoint = "system/workflows/{parentId}/events"
    display_fields = ["id", "eventCondition"]
    required_fields = ["eventCondition"]
    parent_endpoint = "system/workflows"
    parent_id_field = "parentId"

class WorkflowTriggers(BaseEntity):
    endpoint = "system/workflows/{parentId}/triggers"
    display_fields = ["id"]
    required_fields = []
    parent_endpoint = "system/workflows"
    parent_id_field = "parentId"

class CustomReports(BaseEntity):
    endpoint = "system/customReports"
    display_fields = ["id", "reportTitle"]
    required_fields = ["reportTitle"]

class ReportCards(BaseEntity):
    endpoint = "system/reportCards"
    display_fields = ["id", "name", "description"]
    required_fields = ["name"]

class MyCompany(BaseEntity):
    endpoint = "system/myCompany"
    display_fields = ["id", "companyName", "timeZone"]
    required_fields = []
    can_create = False
    can_delete = False

class Links(BaseEntity):
    endpoint = "system/links"
    display_fields = ["id", "name", "url", "tableReferenceId"]
    required_fields = ["name", "url"]

class InOutBoards(BaseEntity):
    endpoint = "system/inOutBoards"
    display_fields = ["id", "member/name", "inOutType"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class InOutTypes(BaseEntity):
    endpoint = "system/inOutTypes"
    display_fields = ["id", "description"]
    required_fields = ["description"]

class Menus(BaseEntity):
    endpoint = "system/menus"
    display_fields = ["id", "caption", "menuLocation"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False

class NotificationRecipients(BaseEntity):
    endpoint = "system/notificationRecipients"
    display_fields = ["id", "identifier", "name"]
    required_fields = ["identifier", "name"]


# =============================================================================
# CATEGORY 11: Accounting (Integrations)
# =============================================================================

class AccountingPackageSetup(BaseEntity):
    endpoint = "finance/accounting/export"
    display_fields = ["id"]
    required_fields = []
    can_create = False
    can_update = False
    can_delete = False


# =============================================================================
# MASTER CATEGORY REGISTRY — drives the hierarchical CLI menu
# =============================================================================

ENTITY_CATEGORIES = {
    "Company & CRM": {
        "Companies": Companies,
        "Contacts": CompanyContacts,
        "Company Notes": CompanyNotes,
        "Company Sites": CompanySites,
        "Company Statuses": CompanyStatuses,
        "Company Types": CompanyTypes,
        "Company Teams": CompanyTeams,
        "Company Groups": CompanyGroups,
        "Company Mgmt Summary": CompanyManagementSummary,
        "Company Type Associations": CompanyTypeAssociations,
        "Contact Types": ContactTypes,
        "Contact Departments": ContactDepartments,
        "Contact Relationships": ContactRelationships,
        "Contact Communications": ContactCommunications,
        "Contact Notes": ContactNotes,
        "Contact Tracks": ContactTracks,
        "Configurations": Configurations,
        "Configuration Statuses": ConfigurationStatuses,
        "Configuration Types": ConfigurationTypes,
        "Company Picker Items": CompanyPickerItems,
        "Management Backups": ManagementBackups,
        "Tracks": Tracks,
        "Track Actions": TrackActions,
        "Portal Configurations": PortalConfigurations,
        "Company Finances": CompanyFinances,
    },
    "Service Desk": {
        "Tickets": ServiceTickets,
        "Boards": ServiceBoards,
        "Board Statuses": BoardStatuses,
        "Board Types": BoardTypes,
        "Board Sub-Types": BoardSubTypes,
        "Board Items": BoardItems,
        "Board Teams": BoardTeams,
        "Board Auto-Assign Resources": BoardAutoAssignResources,
        "Board Excluded Members": BoardExcludedMembers,
        "Board Notifications": BoardNotifications,
        "Board Type/SubType/Item Assoc.": BoardTypeSubTypeItemAssociations,
        "Ticket Notes": TicketNotes,
        "Ticket Tasks": TicketTasks,
        "Ticket Time Entries": TicketTimeEntries,
        "Ticket Schedule Entries": TicketScheduleEntries,
        "Ticket Documents": TicketDocuments,
        "Ticket Configurations": TicketConfigurations,
        "Ticket Merge": TicketMerge,
        "Priorities": Priorities,
        "Sources": ServiceSources,
        "Impacts": Impacts,
        "Severities": Severities,
        "SLAs": SLAs,
        "SLA Priorities": SLAPriorities,
        "Knowledge Base Articles": KnowledgeBaseArticles,
        "Surveys": ServiceSurveys,
        "Service Codes": ServiceCodeAssociations,
        "Service Locations": ServiceLocations,
        "Service Sign-offs": ServiceSignoffs,
        "Service Templates": ServiceTemplates,
    },
    "Sales": {
        "Opportunities": Opportunities,
        "Opportunity Statuses": OpportunityStatuses,
        "Opportunity Types": OpportunityTypes,
        "Opportunity Notes": OpportunityNotes,
        "Opportunity Forecasts": OpportunityForecasts,
        "Opportunity Contacts": OpportunityContacts,
        "Opportunity Teams": OpportunityTeams,
        "Opportunity Ratings": OpportunityRatings,
        "Probabilities": Probabilities,
        "Stages": Stages,
        "Activities": Activities,
        "Activity Statuses": ActivityStatuses,
        "Activity Types": ActivityTypes,
        "Orders": Orders,
        "Order Statuses": OrderStatuses,
        "Sales Roles": SalesRoles,
        "Sales Teams": SalesTeams,
        "Commissions": Commissions,
        "Sales Quotas": SalesQuotas,
    },
    "Finance & Billing": {
        "Agreements": Agreements,
        "Agreement Types": AgreementTypes,
        "Agreement Additions": AgreementAdditions,
        "Agreement Adjustments": AgreementAdjustments,
        "Agreement Board Defaults": AgreementBoardDefaults,
        "Agreement Sites": AgreementSites,
        "Agreement Work Role Excl.": AgreementWorkRoleExclusions,
        "Agreement Work Type Excl.": AgreementWorkTypeExclusions,
        "Agreement Work Roles": AgreementWorkRoles,
        "Agreement Work Types": AgreementWorkTypes,
        "Invoices": Invoices,
        "Invoice Payments": InvoicePayments,
        "GL Accounts": GLAccounts,
        "Billing Cycles": BillingCycles,
        "Billing Setups": BillingSetups,
        "Billing Terms": BillingTerms,
        "Tax Codes": TaxCodes,
        "Tax Code Levels": TaxCodeLevels,
        "Currencies": Currencies,
        "Delivery Methods": DeliveryMethods,
        "Accounting Batches": AccountingBatches,
        "Unposted Expenses": AccountingUnpostedExpenses,
        "Unposted Invoices": AccountingUnpostedInvoices,
        "Unposted Procurements": AccountingUnpostedProcurements,
    },
    "Project": {
        "Projects": Projects,
        "Project Phases": ProjectPhases,
        "Project Notes": ProjectNotes,
        "Project Team Members": ProjectTeamMembers,
        "Project Contacts": ProjectContacts,
        "Project Statuses": ProjectStatuses,
        "Project Boards": ProjectBoards,
        "Project Board Team Members": ProjectBoardTeamMembers,
        "Project Security Roles": ProjectSecurityRoles,
        "Project Tickets": ProjectTickets,
    },
    "Time & Expense": {
        "Time Entries": TimeEntries,
        "Time Sheets": TimeSheets,
        "Time Accruals": TimeAccruals,
        "Time Period Setups": TimePeriodSetups,
        "Expense Entries": ExpenseEntries,
        "Expense Reports": ExpenseReports,
        "Expense Types": ExpenseTypes,
        "Expense Payment Types": ExpensePaymentTypes,
        "Expense Classifications": ExpenseClassifications,
        "Charge Codes": ChargeCodes,
        "Work Roles": WorkRoles,
        "Work Types": WorkTypes,
    },
    "Procurement": {
        "Catalog Items": CatalogItems,
        "Catalog Components": CatalogComponents,
        "Categories": Categories,
        "Sub-Categories": SubCategories,
        "Product Types": ProductTypes,
        "Manufacturers": Manufacturers,
        "Purchase Orders": PurchaseOrders,
        "PO Line Items": PurchaseOrderLineItems,
        "PO Statuses": PurchaseOrderStatuses,
        "Products": ProductComponents,
        "Warehouses": Warehouses,
        "Warehouse Bins": WarehouseBins,
        "RMA Dispositions": RMAs,
        "Shipment Methods": ShipmentMethods,
        "Units of Measure": UnitOfMeasures,
        "Pricing Schedules": PricingSchedules,
        "Adjustments": Adjustments,
        "Adjustment Details": AdjustmentDetails,
    },
    "Marketing": {
        "Campaigns": Campaigns,
        "Campaign Statuses": CampaignStatuses,
        "Campaign Types": CampaignTypes,
        "Campaign Sub-Types": CampaignSubTypes,
        "Campaign Audits": CampaignAudits,
        "Campaign Emails Opened": CampaignEmailsOpened,
        "Campaign Forms Submitted": CampaignFormsSubmitted,
        "Campaign Links Clicked": CampaignLinksClicked,
        "Groups": Groups,
        "Group Companies": GroupCompanies,
        "Group Contacts": GroupContacts,
    },
    "Schedule": {
        "Schedule Entries": ScheduleEntries,
        "Schedule Statuses": ScheduleStatuses,
        "Schedule Types": ScheduleTypes,
        "Schedule Colors": ScheduleColors,
        "Schedule Reminder Times": ScheduleReminderTimes,
        "Calendars": Calendars,
        "Calendar Info": CalendarInfos,
        "Holiday Lists": HolidayLists,
        "Holidays": Holidays,
        "Portal Calendars": SchedulePortalCalendars,
    },
    "System & Admin": {
        "Members": Members,
        "Member Deactivations": MemberDeactivations,
        "Callbacks": Callbacks,
        "Audit Trail": AuditTrail,
        "CW Hosted Setups": ConnectWiseHostedSetups,
        "Documents": Documents,
        "Document Types": DocumentTypes,
        "Email Connectors": EmailConnectors,
        "Security Roles": SecurityRoles,
        "System Info": Info,
        "Departments": Departments,
        "Locations": Locations,
        "Location Departments": LocationDepartments,
        "Location Work Roles": LocationWorkRoles,
        "Workflows": Workflows,
        "Workflow Actions": WorkflowActions,
        "Workflow Events": WorkflowEvents,
        "Workflow Triggers": WorkflowTriggers,
        "Custom Reports": CustomReports,
        "Report Cards": ReportCards,
        "My Company": MyCompany,
        "Links": Links,
        "In/Out Boards": InOutBoards,
        "In/Out Types": InOutTypes,
        "Menus": Menus,
        "Notification Recipients": NotificationRecipients,
    },
    "Accounting": {
        "Accounting Package Setup": AccountingPackageSetup,
        "Accounting Batches": AccountingBatches,
        "Unposted Expenses": AccountingUnpostedExpenses,
        "Unposted Invoices": AccountingUnpostedInvoices,
        "Unposted Procurements": AccountingUnpostedProcurements,
    },
}
