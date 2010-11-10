#import "MensaParser.h"
#import "MensaAppDelegate.h"
#import "Mensa.h"

@implementation MensaParser

- (MensaParser *) initMensaParser {
	
	[super init];
	
	appDelegate = (MensaAppDelegate *)[[UIApplication sharedApplication] delegate];
	
	return self;
}

- (void)parser:(NSXMLParser *)parser didStartElement:(NSString *)elementName 
  namespaceURI:(NSString *)namespaceURI qualifiedName:(NSString *)qualifiedName 
	attributes:(NSDictionary *)attributeDict {
	
	if([elementName isEqualToString:@"mensa"]) {
		//Initialize the array.
		appDelegate.mensas = [[NSMutableArray alloc] init];
	}
	else if([elementName isEqualToString:@"essen"]) {
		
		//Initialize the mensa.
		aMensa = [[Mensa alloc] init];
		
		//Extract the attribute here.
		aMensa.essenID = [[attributeDict objectForKey:@"id"] integerValue];
		
		NSLog(@"Reading id value :%i", aMensa.essenID);
	}
	
	NSLog(@"Processing Element: %@", elementName);
}

- (void)parser:(NSXMLParser *)parser foundCharacters:(NSString *)string { 
	
	if(!currentElementValue) 
		currentElementValue = [[NSMutableString alloc] initWithString:string];
	else
		[currentElementValue appendString:string];
	
	NSLog(@"Processing Value: %@", currentElementValue);
	
}

- (void)parser:(NSXMLParser *)parser didEndElement:(NSString *)elementName 
  namespaceURI:(NSString *)namespaceURI qualifiedName:(NSString *)qName {
	
	if([elementName isEqualToString:@"mensa"])
		return;
	
	if([elementName isEqualToString:@"essen"]) {
		[appDelegate.mensas addObject:aMensa];
		
		[aMensa release];
		aMensa = nil;
	}
	else 
		[aMensa setValue:currentElementValue forKey:elementName];
	
	[currentElementValue release];
	currentElementValue = nil;
}

- (void) dealloc {
	
	[aMensa release];
	[currentElementValue release];
	[super dealloc];
}

@end
