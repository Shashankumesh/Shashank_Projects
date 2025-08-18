dic = {
    "services": [
        {
            "serviceId": "RegressionTest",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "RegressionTest",
                "description": "A service created for the purposes of verifying all of the fields are returned from the api during regression testing.",
                "url": "https://developers.hp.com/stg/jarvis-platform",
                "requiredPlugins": [
                    "Auth",
                    "DataCollection",
                    "Device",
                    "DocProvider",
                    "EventService",
                    "ServiceRouting"
                ],
                "title": {
                    "es-ES": "Prueba de Regresión",
                    "en-US": "Regression Test"
                },
                "iconUrl": "https://developers.hp.com/stg/jarvis-platform",
                "serviceRole": "Regression",
                "version": 0,
                "hideNativeNavbar": True,
                "isVisible": True
            }
        },
        {
            "serviceId": "owsc-ntv-yeti-activation",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "owsc-ntv-yeti-activation",
                "description": "Yeti Activation Onboarding Stage",
                "serviceRole": "DeviceOnboarding",
                "version": 0,
                "hideNativeNavbar": True,
                "isVisible": True
            }
        },
        {
            "serviceId": "UserTenantOnboarding",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "OnboardingMFE",
                "description": "User Tenant Onboarding",
                "url": "https://onboardingcenter.stage.portalshell.int.hp.com/user-tenant-onboarding",
                "requiredPlugins": [
                    "Auth",
                    "ServiceRouting"
                ],
                "version": 0,
                "hideNativeNavbar": True,
                "isVisible": True
            }
        },
        {
            "serviceId": "TextEdit",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "TextEdit",
                "description": "Allows Text to be editted on a webview and the output is an image.",
                "url": "https://static.tropos-rnd.com/pepper/text-react-webapp-stg/latest/index.html",
                "requiredPlugins": [
                    "DataCollection",
                    "DocProvider",
                    "EventService",
                    "ServiceRouting"
                ],
                "serviceRole": "DocTransformer",
                "version": 0,
                "hideNativeNavbar": True,
                "isVisible": True
            }
        },
        {
            "serviceId": "HPX_Scribble",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "HPX_Scribble",
                "description": "Create and merge marks onto documents",
                "url": "https://hpx.stage.portalshell.int.hp.com/scribble",
                "requiredPlugins": [
                    "Auth",
                    "Console",
                    "Device",
                    "DocProvider",
                    "EventService",
                    "ServiceRouting"
                ],
                "serviceRole": "DocTransformer",
                "version": 0,
                "hideNativeNavbar": False,
                "isVisible": True
            }
        },
        {
            "serviceId": "app-ntv-exitoobe",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "app-ntv-exitoobe",
                "description": "Exit OOBE Onboarding Stage, native service",
                "serviceRole": "DeviceOnboarding",
                "version": 0,
                "hideNativeNavbar": True,
                "isVisible": True
            }
        },
        {
            "serviceId": "Softfax",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "Softfax",
                "description": "The Softfax is a web application that allow users to send PDF and images via Fax.",
                "url": "https://hpx.stage.portalshell.int.hp.com/softfax",
                "requiredPlugins": [
                    "Auth",
                    "Console",
                    "Device",
                    "DocProvider",
                    "EventService",
                    "Printer",
                    "ServiceRouting"
                ],
                "serviceRole": "DocTransformer",
                "version": 0,
                "hideNativeNavbar": True,
                "isVisible": True
            }
        },
        {
            "serviceId": "HPX_Redaction",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "HPX_Redaction",
                "description": "This service offers HPX users the ability to redact documents, manually hiding PII data using the user interface. The redaction actions are performed to the document based on the original document image and OCR structure output from the HPPK OCR (HPScan SDK).",
                "url": "https://static.tropos-rnd.com/shortcuts/react-redaction-webapp-stg/latest/index.html",
                "requiredPlugins": [
                    "DataCollection",
                    "DocProvider",
                    "EventService",
                    "ServiceRouting"
                ],
                "serviceRole": "DocTransformer",
                "version": 0,
                "hideNativeNavbar": True,
                "isVisible": True
            }
        },
        {
            "serviceId": "HPX_Shortcuts",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "HPX_Shortcuts",
                "description": "This app allows you to create shortcuts, such as sending a print command, uploading to the cloud, and emailing with a single click.",
                "url": "https://hpx.stage.portalshell.int.hp.com/shortcuts",
                "requiredPlugins": [
                    "Auth",
                    "AuthBrowser",
                    "Device",
                    "EventService",
                    "GetPrinterData",
                    "ServiceRouting",
                    "ValueStore"
                ],
                "version": 0,
                "hideNativeNavbar": True,
                "isVisible": True
            }
        },
        {
            "serviceId": "OnboardingCenter",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "OnboardingCenter",
                "description": "OnboardingCenter Service",
                "url": "https://onboardingcenter.stage.portalshell.int.hp.com/app-onboarding",
                "requiredPlugins": [
                    "Auth",
                    "Device",
                    "EventService",
                    "ServiceRouting"
                ],
                "version": 0,
                "hideNativeNavbar": True,
                "isVisible": True
            }
        },
        {
            "serviceId": "Redaction",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "Redaction",
                "description": "This service offers to users the ability to redact documents, manually hiding PII data using the user interface. The redaction actions are performed to the document based on the original document image and OCR structure output from the HPPK OCR (HPScan SDK).",
                "url": "https://static.tropos-rnd.com/pepper/redaction-react-webapp-stg/latest/index.html",
                "requiredPlugins": [
                    "DataCollection",
                    "DocProvider",
                    "EventService",
                    "ServiceRouting"
                ],
                "serviceRole": "DocTransformer",
                "version": 0,
                "hideNativeNavbar": True,
                "isVisible": True
            }
        },
        {
            "serviceId": "FirmwareUpdateUI",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "FirmwareUpdate UI web App",
                "description": "To notify user about firmware update for a selected printer",
                "url": "https://static.tropos-rnd.com/jarvis/react-firmware-update-ui-stg/latest/index.html",
                "requiredPlugins": [
                    "Auth",
                    "Device",
                    "EventService",
                    "ServiceRouting"
                ],
                "version": 0,
                "hideNativeNavbar": False,
                "isVisible": True
            }
        },
        {
            "serviceId": "BootstrapController",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "BootstrapController",
                "description": "Bootstrap setup for printer onboarding. This will retrieve the printer resources, create a session with OD, and launch OnboardingCenter.",
                "url": "https://static.hpsmart.com/jarvis/react-oobe-bootstrap-controller-stg/latest/index.html",
                "requiredPlugins": [
                    "Auth",
                    "Device",
                    "EventService"
                ],
                "requiredServices": [
                    "OnboardingCenter"
                ],
                "version": 0,
                "hideNativeNavbar": True,
                "isVisible": False
            }
        },
        {
            "serviceId": "HPX_TextExtract",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "HPX_TextExtract",
                "description": "This MFE allows HPX users to edit text extracted from a scanned document and output the resulting file as an image.",
                "url": "https://hpx.stage.portalshell.int.hp.com/text-extract",
                "requiredPlugins": [
                    "DataCollection",
                    "DocProvider",
                    "EventService",
                    "ServiceRouting"
                ],
                "serviceRole": "DocTransformer",
                "version": 0,
                "hideNativeNavbar": True,
                "isVisible": True
            }
        },
        {
            "serviceId": "FirmwareUpdatePsaDriver",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "PSA Driver",
                "description": "This service is an application that manages firmware and printer driver updates, using Micro Frontends (MFE) for modularity.",
                "url": "https://hpx.stage.portalshell.int.hp.com/us/en/psa-firmware-update",
                "requiredPlugins": [
                    "EventService"
                ],
                "version": 0,
                "hideNativeNavbar": False,
                "isVisible": True
            }
        },
        {
            "serviceId": "HPX_CloudScans",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "HPX_CloudScans",
                "description": "HPX MFE that provides the user with a list of Scan jobs executed using the HP Cloud (Tenzing) and started at printer's control panel.",
                "url": "https://hpx.stage.portalshell.int.hp.com/cloudscans",
                "requiredPlugins": [
                    "Auth",
                    "Device",
                    "DocProvider",
                    "EventService",
                    "ServiceRouting"
                ],
                "serviceRole": "DocSource",
                "version": 0,
                "hideNativeNavbar": True,
                "isVisible": True
            }
        },
        {
            "serviceId": "CloudScans",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "CloudScans",
                "description": "Provides a list of Scan jobs executed using the HP Cloud (tenzing) and started at printer control panel.",
                "url": "https://static.tropos-rnd.com/monetization/cloudscans-react-webapp-stg/latest/index.html",
                "requiredPlugins": [
                    "Auth",
                    "Device",
                    "DocProvider",
                    "EventService",
                    "ServiceRouting"
                ],
                "serviceRole": "DocSource",
                "version": 0,
                "hideNativeNavbar": True,
                "isVisible": True
            }
        },
        {
            "serviceId": "Scribble",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "Scribble",
                "description": "Allows users to insert drawed marks on top of a document (pdf or image) and returns the merged document",
                "url": "https://scribble-stage.ext.hp.com/",
                "requiredPlugins": [
                    "Auth",
                    "Console",
                    "Device",
                    "DocProvider",
                    "EventService",
                    "ServiceRouting"
                ],
                "serviceRole": "DocTransformer",
                "version": 0,
                "hideNativeNavbar": True,
                "isVisible": True
            }
        },
        {
            "serviceId": "UserOnboardingApp",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "UserOnboardingApp",
                "description": "React App wrapper for the 'react-user-onboarding' component.",
                "url": "https://static.hpsmart.com/jarvis/user-onboarding-app-stg/latest/index.html",
                "requiredPlugins": [
                    "Auth",
                    "EventService"
                ],
                "version": 0,
                "hideNativeNavbar": True,
                "isVisible": True
            }
        },
        {
            "serviceId": "FirmwareUpdateController",
            "latestManifestVersion": 0,
            "manifest": {
                "name": "FirmwareUpdateController",
                "description": "A web app that allows the firmware update process to be handled and applied.",
                "url": "https://static.hpsmart.com/jarvis/react-firmware-update-controller-stg/latest/index.html",
                "requiredPlugins": [
                    "Auth",
                    "EventService",
                    "ServiceRouting",
                    "ValueStore"
                ],
                "requiredServices": [
                    "FirmwareUpdateUI"
                ],
                "version": 0,
                "hideNativeNavbar": True,
                "isVisible": False
            }
        }
    ]
}

print(len(dic["services"]))
for i in dic["services"]:
    print(i)