using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using SwiftTransferAPI.Models;
using System.Reflection;
using System.Globalization;
using System.Text;
using Newtonsoft.Json;

namespace SwiftTransferAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class SwiftTransfersController : ControllerBase
    {
        private readonly SwiftTransferContext _context;

        public SwiftTransfersController(SwiftTransferContext context)
        {
            _context = context;
        }

        private List<T> Search<T>(string value, List<T> data)
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

        private List<T> Paginate<T>(uint offset, uint limit, List<T> data)
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

        private List<T> Sort<T>(string key, List<T> data)
        {
            if (key[0] != '-')
                return data.OrderBy(d => d.GetType().GetProperty(key).GetValue(d)).ToList();
            else
            {
                key = key.Replace("-", "");
                return data.OrderByDescending(d => d.GetType().GetProperty(key).GetValue(d)).ToList();
            }
        }


        // GET: api/SwiftTransfers
        [HttpGet]
        public async Task<ActionResult<IEnumerable<SwiftTransfer>>> GetSwiftTransfers([FromQuery(Name = "sort_by")] string sort_by = "", [FromQuery(Name = "search")] string search = "", [FromQuery(Name = "offset")] uint offset = 0, [FromQuery(Name = "limit")] uint limit = 25)
        {
            var result = _context.SwiftTransfers.ToList();
            int old_count = _context.SwiftTransfers.ToList().Count;
            bool changed = false;
            if (sort_by != "")
            {
                if ((sort_by[0] != '-' && typeof(SwiftTransfer).GetProperty(sort_by) == null) || (sort_by[0] == '-' && typeof(SwiftTransfer).GetProperty(sort_by.Replace("-", "")) == null))
                    return BadRequest("No such property to sort!");
                result = Sort<SwiftTransfer>(sort_by, result);
                changed = true;
            }
            result = Paginate<SwiftTransfer>(offset, limit, result);
            if (result.Count != old_count)
                changed = true;
            //if (sort_by != "")
            //{
            //    //if ((sort_by[0] != '-' && typeof(SwiftTransfer).GetProperty(sort_by) == null) || (sort_by[0] == '-' && typeof(SwiftTransfer).GetProperty(sort_by.Replace("-", "")) == null))
            //    //    return BadRequest("No such property to sort!");
            //    //result = Sort<SwiftTransfer>(sort_by, result);
            //    //changed = true;
            //}
            if (search != "")
            {
                result = Search<SwiftTransfer>(search, result);
                changed = true;
            }
            if (changed)
                return Ok(new { data = result.AsParallel(), count = _context.SwiftTransfers.ToList().Count, offset = offset, limit = limit, returned = result.Count });
            return Ok(new { data = await _context.SwiftTransfers.ToListAsync(), count = _context.SwiftTransfers.ToList().Count, offset = offset, limit = limit });
        }


        // GET: api/SwiftTransfers/5
        [HttpGet("{id}")]
        public async Task<ActionResult<SwiftTransfer>> GetSwiftTransfer(int id)
        {
            var swiftTransfer = await _context.SwiftTransfers.FindAsync(id);

            if (swiftTransfer == null)
            {
                return NotFound($"This id doesn't exist: {id}");
            }
            return swiftTransfer;
        }

        // PUT: api/SwiftTransfers/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutSwiftTransfer(int id, SwiftTransfer swiftTransfer)
        {
            string mes;
            mes = Validation.IsValidObject(swiftTransfer);
            if (id != swiftTransfer.id)
            {
                return NotFound($"This id doesn't exist: {id}");
            }
            if (mes != "")
            {
                return BadRequest(mes);
            }
            else
            {
                _context.Entry(swiftTransfer).State = EntityState.Modified;

                try
                {
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!SwiftTransferExists(id))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
            }

            return Ok(new {message="Successfully edited", statuscode=200});
        }

        // POST: api/SwiftTransfers
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<SwiftTransfer>> PostSwiftTransfer(SwiftTransfer swiftTransfer)
        {
            string mes;
            mes = Validation.IsValidObject(swiftTransfer);
            if (mes == "")
            {
                if (await _context.SwiftTransfers.FindAsync(swiftTransfer.id) != null)
                    return BadRequest("This id already exists!");
                _context.SwiftTransfers.Add(swiftTransfer);
                await _context.SaveChangesAsync();

                //return CreatedAtAction("GetSwiftTransfer", new { id = swiftTransfer.id }, swiftTransfer);
                return Ok(new { message = "Successfully created", statuscode = 200 });
            }
            else
                return BadRequest(mes);
        }

        // DELETE: api/SwiftTransfers/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteSwiftTransfer(int id)
        {
            var swiftTransfer = await _context.SwiftTransfers.FindAsync(id);
            if (swiftTransfer == null)
            {
                return NotFound($"This id doesn't exist: {id}");
            }

            _context.SwiftTransfers.Remove(swiftTransfer);
            await _context.SaveChangesAsync();
            return Ok(new { message = "Successfully deleted", statuscode = 200 });
        }


        private bool SwiftTransferExists(int id)
        {
            return _context.SwiftTransfers.Any(e => e.id == id);
        }
    }
}
