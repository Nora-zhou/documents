package io.flood.selenium;

import java.net.URL;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriverException;

import org.openqa.selenium.remote.Augmenter;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;

import io.flood.selenium.FloodSump;

public class LoadTest  {
  public static void main(String[] args) throws Exception {
    int iterations = 0;

    // Create a new instance of the html unit driver
    // Notice that the remainder of the code relies on the interface,
    // not the implementation.
    WebDriver driver = new RemoteWebDriver(new URL("http://" + System.getenv("WEBDRIVER_HOST") + ":" + System.getenv("WEBDRIVER_PORT") + "/wd/hub"), DesiredCapabilities.chrome());
    JavascriptExecutor js = (JavascriptExecutor)driver;

    // Create a new instance of the Flood IO agent
    FloodSump flood = new FloodSump();

    // Inform Flood IO the test has started
    flood.started();
    new WebDriverWait(driver,5).until(ExpectedConditions.presenceOfElementLocated(By.id("i0116")));
	driver.findElement(By.id("i0116")).sendKeys("nozhou@deloitte.com.cn");
	//Thread.sleep(1000);
	new WebDriverWait(driver,5).until(ExpectedConditions.presenceOfElementLocated(By.id("idSIButton9")));
	driver.findElement(By.id("idSIButton9")).click();
	//Thread.sleep(3000);
	new WebDriverWait(driver,5).until(ExpectedConditions.presenceOfElementLocated(By.id("passwordInput")));
	driver.findElement(By.id("passwordInput")).sendKeys("Zjh2146406!");
	driver.findElement(By.id("submitButton")).click();
	String title=driver.getTitle();
	boolean issuccess = false;
	if( title=="µÇÂ¼ / Login111"){
		issuccess=true;
	};
	assert issuccess;
    // It's up to you to control test duration / iterations programatically.
    while( iterations < 1000 ) {
      try {
        // And now use this to visit the target site
        driver.get("https://loadtest.flood.io/usertiming");

        // Log a passed transaction in Flood IO
        flood.passed_transaction(driver);

        // Log a custom mark from the User Timing API
        flood.get_mark(driver, "mark_headers_loaded");

        // Log a custom measure from the User Timing API
        flood.get_measure(driver, "measure_page_load");

        iterations++;

        // Good idea to introduce some form of pacing / think time into your scripts
        Thread.sleep(3000);
      } catch(InterruptedException e) {
        Thread.currentThread().interrupt();
        String[] lines = e.getMessage().split("\\r?\\n");
        System.err.println("Browser terminated early: " + lines[0]);
      } catch (WebDriverException e) {
        String[] lines = e.getMessage().split("\\r?\\n");
        System.err.println(lines[0]);
      }
    }

    driver.quit();

    // Inform Flood IO the test has finished
    flood.finished();
  }
}