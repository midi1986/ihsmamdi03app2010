#import "MensaDetailViewController.h"
#import "MensaKategorie.h"
#import "MensaEssen.h"

@implementation MensaDetailViewController

@synthesize mensaTag;

/*
// Override initWithNibName:bundle: to load the view using a nib file then perform additional customization that is not appropriate for viewDidLoad.
- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil {
    if (self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil]) {
        // Custom initialization
    }
    return self;
}
*/

/*
// Implement loadView to create a view hierarchy programmatically.
- (void)loadView {
}
*/


// Implement viewDidLoad to do additional setup after loading the view.
- (void)viewDidLoad {
    [super viewDidLoad];
	
	self.title = @"Mensa Detail";
}

- (void)viewWillAppear:(BOOL)animated {
	[super viewWillAppear:animated];
	
	[tableView reloadData];
}


- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation {
    // Return YES for supported orientations
    return (interfaceOrientation == UIInterfaceOrientationPortrait);
}


- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning]; // Releases the view if it doesn't have a superview
    // Release anything that's not essential, such as cached data
}

- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView {
    return [mensaTag.mensaKategorien count];
}


- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
	
	MensaKategorie *mensaKategorie = [mensaTag.mensaKategorien objectAtIndex:section];
    
	return [mensaKategorie.mensaEssens count];
}

- (UITableViewCell *)tableView:(UITableView *)tv cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    
    static NSString *CellIdentifier = @"Cell";
    
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    if (cell == nil) {
        cell = [[[UITableViewCell alloc] initWithFrame:CGRectZero reuseIdentifier:CellIdentifier] autorelease];
    }
	
	
	MensaKategorie *mensaKategorie = [mensaTag.mensaKategorien objectAtIndex:indexPath.section];
	MensaEssen *mensaEssen = [mensaKategorie.mensaEssens objectAtIndex:indexPath.row];
	
	cell.text = mensaEssen.name;
	
	return cell;
}

- (NSString *)tableView:(UITableView *)tblView titleForHeaderInSection:(NSInteger)section {
	
	MensaKategorie *mensaKategorie = [mensaTag.mensaKategorien objectAtIndex:section];
	
	return mensaKategorie.name;
}

- (void)dealloc {
	
	[mensaTag release];
	[tableView release];
    [super dealloc];
}


@end
