using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using SwiftTransferAPI.Models;
using System.Web.Http;
using System.Reflection;
using System.Globalization;
using System.Text;
using Newtonsoft.Json;

namespace SwiftTransferAPI.Controllers
{
    public class SwiftTransfersControllerTest : ApiController
    {
        List<SwiftTransfer> transfers = new List<SwiftTransfer>();

        public SwiftTransfersControllerTest() { }

        public SwiftTransfersControllerTest(List<SwiftTransfer> transfers)
        {
            this.transfers = transfers;
        }

        public IEnumerable<SwiftTransfer> GetAllTransfers()
        {
            return transfers;
        }

        public async Task<IEnumerable<SwiftTransfer>> GetAllTransfersAsync()
        {
            return await Task.FromResult(GetAllTransfers());
        }

        public IHttpActionResult GetTransfer(int id)
        {
            var transfer = transfers.FirstOrDefault((p) => p.id == id);
            if (transfer == null)
            {
                return NotFound();
            }
            return Ok(transfer);
        }

        public async Task<IHttpActionResult> GetTransferAsync(int id)
        {
            return await Task.FromResult(GetTransfer(id));
        }
        public List<T> Search<T>(string value, List<T> data)
        {
            List<T> suitable = new List<T>();
            PropertyInfo[] props = typeof(T).GetProperties();
            for (int i = 0; i < data.Count; i++)
            {
                bool flag = false;
                for (int j = 0; j < props.Length; j++)
                {
                    if (Convert.ToString(props[j].GetValue(data[i])).ToLower().Contains(value.ToLower()))
                        flag = true;
                    if (flag)
                        break;
                }
                if (flag)
                    suitable.Add(data[i]);
            }
            return suitable;
        }

        public async Task<IEnumerable<SwiftTransfer>> GetAllTransfersFindAsync(string value, List<SwiftTransfer> data)
        {
            return await Task.FromResult((IEnumerable<SwiftTransfer>)Search(value,data));
        }

        public async Task<IEnumerable<SwiftTransfer>> GetAllTransfersSortAsync(string key, List<SwiftTransfer> data)
        {
            return await Task.FromResult((IEnumerable<SwiftTransfer>)Sort(key, data));
        }

        public async Task<IEnumerable<SwiftTransfer>> GetAllTransfersPaginateAsync(uint offset, uint limit, List<SwiftTransfer> data)
        {
            return await Task.FromResult((IEnumerable<SwiftTransfer>)Paginate(offset, limit, data));
        }
        public List<T> Paginate<T>(uint offset, uint limit, List<T> data)
        {
            int real_limit;
            if (((offset + 1) * limit - limit) >= data.Count())
                return new List<T>();
            if (data.Count() - ((offset + 1) * limit - limit) < limit)
                real_limit = data.Count() - Convert.ToInt32(((offset + 1) * limit - limit));
            else
                real_limit = Convert.ToInt32(limit);
            return data.GetRange(Convert.ToInt32((offset + 1) * limit - limit), Convert.ToInt32(real_limit));
        }

        public List<T> Sort<T>(string key, List<T> data)
        {
            if (key[0] != '-')
                return data.OrderBy(d => d.GetType().GetProperty(key).GetValue(d)).ToList();
            else
            {
                key = key.Replace("-", "");
                return data.OrderByDescending(d => d.GetType().GetProperty(key).GetValue(d)).ToList();
            }
        }
    }
}
