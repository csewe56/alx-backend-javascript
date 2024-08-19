/**
 * Contains the miscellaneous route handlers.
 * @author Charles  O. Sewe <https://github.com/csewe56>
 */
class AppController {
  static getHomepage(request, response) {
    response.status(200).send('Hello Holberton School!');
  }
}

export default AppController;
module.exports = AppController;
