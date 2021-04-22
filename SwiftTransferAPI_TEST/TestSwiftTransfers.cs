using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Web.Http.Results;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using SwiftTransferAPI.Controllers;
using SwiftTransferAPI.Models;
using System.Data;
using Microsoft.EntityFrameworkCore;

namespace SwiftTransferApi_TEST
{
    [TestClass]
    public class TestSwiftTransfers
    {
        private List<SwiftTransfer> GetTestTransfers()
        {
            var _context = new List<SwiftTransfer>();
            _context.Add(new SwiftTransfer { id = 433792, amount = 8723.56, fee_amount = 765.0, currency = (SwiftTransferAPI.Currency)Enum.Parse(typeof(SwiftTransferAPI.Currency), "eur"), iban = "UA43 9755 0101 2110", holder = "Elon Musk", date = new DateTime(2020, 2, 8, 7, 32, 56) });
            _context.Add(new SwiftTransfer { id = 237912, amount = 5678.12, fee_amount = 348.2, currency = (SwiftTransferAPI.Currency)Enum.Parse(typeof(SwiftTransferAPI.Currency), "uah"), iban = "UA23 9755 0101 2110", holder = "Ivan Musk", date = new DateTime(2019, 2, 4, 5, 32, 16) });
            _context.Add(new SwiftTransfer { id = 930012, amount = 5343.43, fee_amount = 111.0, currency = (SwiftTransferAPI.Currency)Enum.Parse(typeof(SwiftTransferAPI.Currency), "eur"), iban = "UA13 9755 0101 2110", holder = "Hawr Musk", date = new DateTime(2017, 3, 1, 7, 32, 56) });
            _context.Add(new SwiftTransfer { id = 555555, amount = 4364.56, fee_amount = 765.4, currency = (SwiftTransferAPI.Currency)Enum.Parse(typeof(SwiftTransferAPI.Currency), "usd"), iban = "UA33 9755 0101 2110", holder = "Iyil Musk", date = new DateTime(2020, 2, 4, 7, 32, 16) });
            _context.Add(new SwiftTransfer { id = 222122, amount = 9347.56, fee_amount = 476.0, currency = (SwiftTransferAPI.Currency)Enum.Parse(typeof(SwiftTransferAPI.Currency), "usd"), iban = "UA53 9755 0101 2110", holder = "Bors Musk", date = new DateTime(2010, 5, 5, 7, 32, 11) });
            return _context;
        }
        [TestMethod]
        public void GetAllTransfers_ShouldReturnAllTransfers()
        {
            var testTransfers = GetTestTransfers();
            var controller = new SwiftTransfersControllerTest(testTransfers);

            var result = controller.GetAllTransfers() as List<SwiftTransfer>;
            Assert.AreEqual(testTransfers.Count, result.Count);
        }
        [TestMethod]
        public async Task GetAllTransfersAsync_ShouldReturnAllTransfers()
        {
            var testTransfers = GetTestTransfers();
            var controller = new SwiftTransfersControllerTest(testTransfers);

            var result = await controller.GetAllTransfersAsync() as List<SwiftTransfer>;
            Assert.AreEqual(testTransfers.Count, result.Count);
        }

        [TestMethod]
        public void GetTransfer_ShouldReturnCorrectTransfer()
        {
            var testTransfers = GetTestTransfers();
            var controller = new SwiftTransfersControllerTest(testTransfers);

            var result = controller.GetTransfer(237912) as OkNegotiatedContentResult<SwiftTransfer>;
            Assert.IsNotNull(result);
            Assert.AreEqual(testTransfers[1].holder, result.Content.holder);
        }

        [TestMethod]
        public async Task GetTransferAsync_ShouldReturnCorrectTransfer()
        {
            var testTransfers = GetTestTransfers();
            var controller = new SwiftTransfersControllerTest(testTransfers);

            var result = await controller.GetTransferAsync(930012) as OkNegotiatedContentResult<SwiftTransfer>;
            Assert.IsNotNull(result);
            Assert.AreEqual(testTransfers[2].holder, result.Content.holder);
        }

        [TestMethod]
        public void GetTransfer_ShouldNotFindTransfer()
        {
            var controller = new SwiftTransfersControllerTest(GetTestTransfers());
            var result = controller.GetTransfer(999);
            Assert.IsInstanceOfType(result, typeof(NotFoundResult));
        }


        [TestMethod]
        public void GetTransfersFind_ShouldFindTransfers()
        {
            var testTransfers = GetTestTransfers();
            var controller = new SwiftTransfersControllerTest(testTransfers);

            var result = controller.Search("3001", testTransfers);
            Assert.AreEqual(testTransfers[2].holder, result[0].holder);
        }

        [TestMethod]
        public async Task GetTransfersFindAsync_ShouldFindTransfers()
        {
            var testTransfers = GetTestTransfers();
            var controller = new SwiftTransfersControllerTest(testTransfers);

            var result = await controller.GetAllTransfersFindAsync("3001", testTransfers) as List<SwiftTransfer>;
            Assert.AreEqual(1, result.Count);
        }

        [TestMethod]
        public void GetTransferSorted_ShouldSortTransfer()
        {
            var testTransfers = GetTestTransfers();
            var controller = new SwiftTransfersControllerTest(testTransfers);

            var result = controller.Sort("-id", testTransfers);
            Assert.AreEqual(testTransfers[3].holder, result[1].holder);
        }

        [TestMethod]
        public async Task GetTransferSortedAsync_ShouldSortTransfer()
        {
            var testTransfers = GetTestTransfers();
            var controller = new SwiftTransfersControllerTest(testTransfers);

            var result = await controller.GetAllTransfersSortAsync("-id", testTransfers) as List<SwiftTransfer>;
            Assert.AreEqual(testTransfers[3].holder, result[1].holder);
        }

        [TestMethod]
        public void GetTransferPaginated_ShouldPaginateTransfer()
        {
            var testTransfers = GetTestTransfers();
            var controller = new SwiftTransfersControllerTest(testTransfers);

            var result = controller.Paginate(1, 4, testTransfers);
            Assert.AreEqual(testTransfers[4].holder, result[0].holder);
        }

        [TestMethod]
        public async Task GetTransferPaginatedAsync_ShouldPaginateTransfer()
        {
            var testTransfers = GetTestTransfers();
            var controller = new SwiftTransfersControllerTest(testTransfers);

            var result = await controller.GetAllTransfersPaginateAsync(1, 4, testTransfers) as List<SwiftTransfer>;
            Assert.AreEqual(testTransfers[4].holder, result[0].holder);
        }
    }
}
