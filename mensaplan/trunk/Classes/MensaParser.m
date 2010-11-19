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
	NSLog(@"Processing Start Element: %@", elementName);
	
	if([elementName isEqualToString:@"mensaPlan"]) {
		
		appDelegate.mensaPlan = [[MensaPlan alloc] init];
		appDelegate.mensaPlan.mensaTage = [[NSMutableArray alloc] init];
		
	} else if ([elementName isEqualToString:@"mensaTag"]) {
		NSLog(@"MensaTag!: ");

		mensaTag = [[MensaTag alloc] init];
		mensaTag.name = [attributeDict valueForKey:@"name"];
		mensaTag.mensaKategorien = [[NSMutableArray alloc] init];
		
		NSLog(@"Reading day of week value :%@", mensaTag.name);
		
	} else if ([elementName isEqualToString:@"mensaKategorie"]) {
		
		mensaKategorie = [[MensaKategorie alloc] init];
		mensaKategorie.name = [attributeDict valueForKey:@"name"];
		mensaKategorie.mensaEssens = [[NSMutableArray alloc] init];
		
		NSLog(@"Reading mensaKategorie name value :%i", mensaKategorie.name);
	} else if ([elementName isEqualToString:@"essen"]) {
		
		mensaEssen = [[MensaEssen alloc] init];
		mensaEssen.essenID = [[attributeDict objectForKey:@"id"] integerValue];
		
		NSLog(@"Reading mensaKategorie mensaEssen.essenID :%i", mensaEssen.essenID);
	}

	

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
	NSLog(@"Processing End Element: %@", elementName);
	if([elementName isEqualToString:@"mensaPlan"]) {
		return;
	} else if([elementName isEqualToString:@"mensaTag"]) {
		[appDelegate.mensaPlan.mensaTage addObject:mensaTag];
		
		[mensaTag release];
		mensaTag = nil;
	} else if([elementName isEqualToString:@"mensaKategorie"]) {
		[mensaTag.mensaKategorien addObject:mensaKategorie];
		
		[mensaKategorie release];
		mensaKategorie = nil;
	} else if([elementName isEqualToString:@"essen"]) {
		[mensaKategorie.mensaEssens addObject:mensaEssen];
		
		[mensaEssen release];
		mensaEssen = nil;
	} else {
		// essen ist das einzige Objekt, dass weitere Eigenschaften besitzt
		
		[mensaEssen setValue:currentElementValue forKey:elementName];
		[currentElementValue release];
		currentElementValue = nil;
	}
  }

- (void) dealloc {
	
	[mensaTag release];
	[mensaKategorie release];
	[mensaEssen release];

	[super dealloc];
}

@end
