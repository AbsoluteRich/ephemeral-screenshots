using System.IO;

namespace EphemeralScreenshots;

/// <summary>
/// Interaction logic for MainWindow.xaml
/// </summary>
public partial class MainWindow
{
    private readonly string _screenshotsFolder = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyPictures), "Screenshots");
        
    public MainWindow()
    {
        InitializeComponent();
    }

    // https://www.c-sharpcorner.com/article/detecting-file-changes-using-filesystemwatcher/
    private void TakeScreenshot_Click(object sender, System.Windows.RoutedEventArgs e)
    {
        FileSystemWatcher watcher = new FileSystemWatcher
        {
            NotifyFilter = NotifyFilters.FileName,
            Path = _screenshotsFolder,
        };
    }
}
