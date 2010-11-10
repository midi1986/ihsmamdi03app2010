#import "MensaAppDelegate.h"
#import "RootViewController.h"
#import "MensaParser.h"

@implementation MensaAppDelegate

@synthesize window;
@synthesize navigationController, mensas;


- (void)applicationDidFinishLaunching:(UIApplication *)application {
	
	
	NSURL *url = [[NSURL alloc] initWithString:@"http://ihsmamdi03app2010.googlecode.com/svn/mensaplan/trunk/data/mensa.xml"];
	NSXMLParser *xmlParser = [[NSXMLParser alloc] initWithContentsOfURL:url];
	
	MensaParser *parser = [[MensaParser alloc] initMensaParser];
	
	[xmlParser setDelegate:parser];
	
	BOOL success = [xmlParser parse];
	
	if(success)
		NSLog(@"No Errors");
	else
		NSLog(@"Error Error Error!!!");
	
	[window addSubview:[navigationController view]];
	[window makeKeyAndVisible];
}


- (void)applicationWillTerminate:(UIApplication *)application {
}


- (void)dealloc {
	[mensas release];
	[navigationController release];
	[window release];
	[super dealloc];
}

@end
