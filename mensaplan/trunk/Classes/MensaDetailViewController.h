#import <UIKit/UIKit.h>

@class Mensa;

@interface MensaDetailViewController : UIViewController {

	IBOutlet UITableView *tableView;
	
	Mensa *aMensa;
}

@property (nonatomic, retain) Mensa *aMensa;

@end
