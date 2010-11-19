//
//  MensaEssen.h
//  Mensa
//
//  Created by emc on 19.11.10.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//

@interface MensaEssen : NSObject {

	NSInteger essenID;

	NSString *sorte;	
	NSString *name;
	NSString *beschreibung;
	NSString *preis;
}

@property (nonatomic, readwrite) NSInteger essenID;

@property (nonatomic, retain) NSString *sorte;
@property (nonatomic, retain) NSString *name;
@property (nonatomic, retain) NSString *beschreibung;
@property (nonatomic, retain) NSString *preis;

@end
